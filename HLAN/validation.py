import logging
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping

import numpy as np
import tensorflow.compat.v1 as tf

from HAN_model_dynamic import HAN
from performance import (
    ModelOutputs,
    ModelPerformance,
    RunningModelPerformance,
    compute_summary_performance,
)


def validate(
    session: tf.Session,
    model: HAN,
    epoch: int,
    num_classes: int,
    feeder: Callable[[], Iterable[Mapping[Any, Any]]],
) -> ModelOutputs:
    logger = logging.getLogger("validation")
    running_performance = RunningModelPerformance.empty()
    all_logits = np.empty((0, num_classes))
    all_predictions = np.empty((0, num_classes))
    all_labels = np.empty((0, num_classes))

    for step, feed_dict in enumerate(feeder()):
        (
            validation_loss_per_batch,
            validation_loss_per_epoch,
            loss,
            precision,
            recall,
            jaccard_index,
            logits,
            predictions,
            labels,
        ) = session.run(
            [
                model.validation_loss_per_batch,
                model.validation_loss_per_epoch,
                model.loss,
                model.precision,
                model.recall,
                model.jaccard_index,
                model.logits,
                model.predictions,
                model.input_y,
            ],
            feed_dict,
        )

        performance = ModelPerformance(
            loss=loss, precision=precision, recall=recall, jaccard_index=jaccard_index
        )
        logger.debug("Current performance: %s", performance)

        running_performance = running_performance + performance
        assert running_performance.count == step + 1

        if step % 50 == 0:
            logger.info(
                "Average performance (epoch %s, step %s): %s",
                epoch,
                step,
                running_performance.average(),
            )

        model.writer.add_summary(validation_loss_per_batch, step)

        if step == 0:  # epoch rolled over
            model.writer.add_summary(validation_loss_per_epoch, epoch)

        all_logits = np.concatenate((all_logits, logits), axis=0)
        all_predictions = np.concatenate((all_predictions, predictions), axis=0)
        all_labels = np.concatenate((all_labels, labels), axis=0)

    logger.info(
        "Average performance (epoch %s, step %s): %s",
        epoch,
        step,
        running_performance.average(),
    )

    return ModelOutputs(
        logits=all_logits, predictions=all_predictions, labels=all_labels
    )


def update_performance(
    ckpt_dir: Path,
    model: HAN,
    session: tf.Session,
    best_micro_f1_score: float,
    epoch: int,
    model_outputs: ModelOutputs,
):
    logger = logging.getLogger("update_performance")

    summary_performance = compute_summary_performance(model_outputs)
    logger.info("Micro ROC-AUC score is %s", summary_performance.micro_roc_auc_score)

    current_learning_rate = session.run(model.learning_rate)

    if summary_performance.micro_f1_score >= best_micro_f1_score:
        logger.info(
            "Micro F1 score improved from %s to %s",
            best_micro_f1_score,
            summary_performance.micro_f1_score,
        )
        saver = tf.train.Saver(max_to_keep=1)
        save_path = ckpt_dir / "model.ckpt"
        logger.info("Saving model checkpoint to %s", save_path)
        saver.save(session, save_path.as_posix(), global_step=epoch)
        best_micro_f1_score = summary_performance.micro_f1_score
    else:
        logger.info(
            "Micro F1 score degraded from %s to %s",
            best_micro_f1_score,
            summary_performance.micro_f1_score,
        )
        _ = session.run([model.learning_rate_decay_half_op])
        new_learning_rate = session.run(model.learning_rate)
        logger.info(
            "Updated learning rate from %s to %s",
            current_learning_rate,
            new_learning_rate,
        )
        current_learning_rate = new_learning_rate

    return best_micro_f1_score, current_learning_rate
