"""Test a trained language detection model

The script loads the trained model from disk and 
uses it to predict a few sentences.
"""
# Author: Francesco Mosconi
# License: Simplified BSD

import sys
import gzip
import dill

# load the trained model and the target names from disk
try:
    with gzip.open('my_model.dill.gz') as fin:
        model, target_names = dill.load(fin)
except:
    print("Couldn't find a saved model. Go back to the exercise and build one!")
    exit(-1)

if len(sys.argv) < 2:
    print("No argument provided, I'll use some test sentences:")
    test_sentences = ['This is a language detection test.',
                      'Test di riconoscimento della lingua.',
                      'Ceci est un test de d\xe9tection de la langue.',
                      'Dies ist ein Test, um die Sprache zu erkennen.',
                      ]
else:
    test_sentences = [sys.argv[1]]

# generate the prediction
predicted = model.predict(test_sentences)

for s, p in zip(test_sentences, predicted):
    print(('Language of "%s" ===> "%s"' % (s, target_names[p])))
