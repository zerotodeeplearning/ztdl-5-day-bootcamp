import argparse
from sklearn.model_selection import train_test_split

from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import Adam
from keras.utils import to_categorical

import wandb
from wandb.keras import WandbCallback

parser = argparse.ArgumentParser()

parser.add_argument('--num_conv_filters', default=128)
parser.add_argument('--num_conv_layers', default=2)
parser.add_argument('--num_convs_per_max_pool', default=1)
parser.add_argument('--dense_size', default=256)
parser.add_argument('--num_dense_layers', default=1)
parser.add_argument('--dropout', default=0.15)
parser.add_argument('--learn_rate', default=0.001)
parser.add_argument('--batch_size', default=64)

hp_set = parser.parse_args()

#############
# Load Data #
#############
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
X_train = X_train.astype('float32') / 255.
X_test = X_test.astype('float32') / 255.

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.10)


########################
# Build Model Function #
########################
def build_compile(config):
    model = Sequential()

    for ci in range(config.num_conv_layers):
        if ci == 0:
            model.add(Conv2D(config.num_conv_filters,
                             config.conv_filter_size,
                             activation=config.activation,
                             padding='same',
                             input_shape=X_train.shape[1:]))
        else:
            model.add(Conv2D(config.num_conv_filters,
                             config.conv_filter_size,
                             activation=config.activation,
                             padding='same'))

        if not ci % config.num_convs_per_max_pool:
            model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())

    for di in range(config.num_dense_layers):
        model.add(Dense(config.dense_size, activation=config.activation))
        model.add(Dropout(config.dropout))

    model.add(Dense(10, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(lr=config.learn_rate),
                  metrics=['accuracy'])

    return model


###########################
# Compile Hyperparameters #
###########################
static_hyper_params = {
    'activation': 'relu',
    'conv_filter_size': 3,
    'num_epochs': 2,
}

wandb.init()

wandb.config.update(static_hyper_params, allow_val_change=True)
wandb.config.update(hp_set, allow_val_change=True)

# build model
model = build_compile(wandb.config)
print(model.summary())
wandb.config.num_model_parameters = model.count_params()

# train model
history = model.fit(
    X_train, y_train,
    batch_size=wandb.config.batch_size,
    epochs=wandb.config.num_epochs,
    verbose=1,
    validation_data=(X_valid, y_valid),
    callbacks=[WandbCallback()]
)