"""Build a language detector model

The goal of this exercise is to train a linear classifier on text features
that represent sequences of up to N consecutive characters so as to be
recognize natural languages by using the frequencies of short character
sequences as 'fingerprints'.

The script saves the trained model to disk for later use
"""
# Author: Olivier Grisel <olivier.grisel@ensta.org>
# License: Simplified BSD
# Adapted by: Francesco Mosconi

import numpy as np
from sklearn.datasets import load_files


# The training data folder must be passed as first argument
try:
    dataset = load_files('./wikidata/short_paragraphs')
except OSError as ex:
    print(ex)
    print("Couldn't import the data, did you unzip the wikidata.zip folder?")
    exit(-1)


# TASK: Split the dataset in training and test set
# (use 20% of the data for test):


# TASK: Build a an vectorizer that splits
# strings into sequence of 1 to 3
# characters instead of word tokens
# using the class TfidfVectorizer


# TASK: Use the function make_pipeline to build a
#       vectorizer / classifier pipeline
#       using the previous analyzer
#       and a classifier of choice.
#       The pipeline instance should be
#       stored in a variable named model


# TASK: Fit the pipeline on the training set


# TASK: Predict the outcome on the testing set.
# Store the result in a variable named y_predicted


# TASK: Print the classification report


# TASK: Print the confusion matrix. Bonus points if you make it pretty.


# TASK: Is the score good? Can you improve it changing
#       the parameters or the classifier?
#       Try using cross validation and grid search

# TASK: Use dill and gzip to persist the trained model in memory.
#       1) gzip.open a file called my_model.dill.gz
#       2) dump to the file both your trained classifier
#          and the target_names of the dataset (for later use)
#    They should be passed as a list [model, dataset.target_names]
