Hi welcome to this repo Reproduce-Explainable-Automated-Medical-Coding.

<h1> Aim </h1>
The main aim of this project is to reproduce the result of Explainable-Automated-Medical-Coding using the latest libraries. Secondary aim is carry out other analysis by doing some variations in the parameters and model to analyse the effect of these variations on the model performance.

<h1> About this repositry </h1>
This repo uses the codes from the main repositry to reproduce the result.
Link for the main repositry - https://github.com/acadTags/Explainable-Automated-Medical-Coding 

The code has been modified to use the latest libraries, Inspiration was taken from this repositry which tries to reproduce the results of the main repositry in a Colab environment.
Link to the repositry - https://github.com/dmcguire81/CS598DL4H

Main the repositry uses the preprocessing steps from CAML-MIMIC repositry which is a neccessary requirement for reprocubility of the main repositry.
Link for CAML-MIMIC repositry - https://github.com/jamesmullenbach/caml-mimic

<h1> Project Setup </h1>
A project setup similar to https://github.com/dmcguire81/CS598DL4H was needed for this project as it provides complete files in one repositry.

Step 1:
Make a standalone repositry

Step 2:
Clone https://github.com/jamesmullenbach/caml-mimic and https://github.com/acadTags/Explainable-Automated-Medical-Coding into the repositry

Step 3:
Using the inpsiration from https://github.com/dmcguire81/CS598DL4H The HLAN was modified to work with latest libraries

Step 4:
Modification of code in caml-mimic to use the latest libraries. Place the data as mentioned in the original repositry and then use the notebook caml-mimic/notebooks/dataproc_mimic_III.ipynb to preprocess the mimic data.

Step 5:
Place the mimiciii_*_50_th0.txt files inside the Explainable-Automated-Medical-Coding/datasets/ along with other requirements mentioned in the Explainable-Automated-Medical-Coding/README.md. using the modified HLAN files run the training.

<h1> Notebook </h1>
I have placed a notebook which replicates the step above, Note the files can be copied using python libraries but here was done manually to avoid any confusion.
