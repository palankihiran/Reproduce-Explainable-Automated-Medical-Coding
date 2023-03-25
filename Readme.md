<h1> Project Description </h1>
This project aims to reproduce the results of the Explainable Automated Medical Coding system as presented in the paper titled "Explainable Automated Medical Coding" by B. Paudel et al. The original paper proposed a system for automatically assigning medical codes to clinical notes using deep learning techniques. By this the reproducibility of the project can be verified.

In this project, we will use the latest libraries and frameworks to recreate the original system and evaluate its performance. By using the latest libraries and dependencies, this project will ensure that the code remains compatible with the latest versions of software and can be run in the future. This can increase the reproducibility of the results and make it easier for others to build upon the work in the future.

<h1> Getting Started </h1>
To get started with this project, follow these steps:

- Make a standalone repositry
- Clone the project repository: git clone https://github.com/acadTags/Explainable-Automated-Medical-Coding.git
- Clone the project repository: git clone https://github.com/jamesmullenbach/caml-mimic.git
- Install the necessary dependencies: pip install -r requirements.txt
- Download the dataset used in the original paper and preprocess it using the instructions in the caml-mimic repository
- Convert the preprocessed .csv files from the caml-mimic to .txt files as required and mentioned in Explainable-Automated-Medical-Coding using the code provided in the Repo_setup.ipnb
- To Train the model, I have listed the commands used to train the model in the Repo_setup.ipynb
- Evaluate the model on the test set and compare the results to those reported in the paper.
<h1> Requirements </h1>
This project requires the following libraries and frameworks:
</br>
- Python 3.7 or higher
- TensorFlow 2.10 or higher
- pandas
- numpy
- matplotlib
- seaborn
- gensil
- tflearn
- tf_slim
- nltk

<h1> Results </h1>
| Model Name and Parameters | Published Result | Obtained Result |
| --- | --- | --- |
| HLAN+LE+sent_split | Micro-F1-score: 74.6%, Micro-ROC-AUC score: 96.9% | Micro-F1-score: 57.51%, Micro-ROC-AUC score: 89.7% |
| HAN+LE | Micro-F1-score: 75.1%, Micro-ROC-AUC score: 97.4% | Micro-F1-score: 58.14%, Micro-ROC-AUC score: 89.8% |
| HA-GRU+LE | Micro-F1-score: 73.4%, Micro-ROC-AUC score: 96.8% | Micro-F1-score: 57.63%, Micro-ROC-AUC score: 89.7% |
| HLAN+LE | Not published | Micro-F1-score: 64.28%, Micro-ROC-AUC score: 92.17% |

<h1> Acknowledgements </h1>
This project is based on the work of B. Paudel et al. as presented in their paper "Explainable Automated Medical Coding". We would like to thank the authors for making their code and dataset available to the public.

<h1> License </h1>
This project is licensed under the MIT License. See the LICENSE file for details.
