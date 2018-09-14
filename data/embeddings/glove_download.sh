# Script to download and extract Glove
# word embeddings. More information at:
# https://nlp.stanford.edu/projects/glove/

# Uncomment the file you'd like to download
EMBEDDINGS=glove.6B
# EMBEDDINGS=glove.42B.300d
# EMBEDDINGS=glove.840B.300d

# download and extract
wget http://nlp.stanford.edu/data/$EMBEDDINGS.zip
unzip $EMBEDDINGS.zip
rm $EMBEDDINGS.zip
