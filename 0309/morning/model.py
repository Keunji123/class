import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train, X_test = X_train / 255, X_test / 255

model = Sequential()
model.add(layers.Flatten(input_shape=(28, 28)))
model.add(layers.Dense(128, activation = 'relu'))
model.add(layers.Dense(64, activation = 'relu'))
model.add(layers.Dense(10, activation = 'softmax'))

model.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

print('MAKE MODEL')
history = model.fit(
    X_train,
    y_train,
    validation_split = 0.2,
    batch_size = 32,
    # validation_data = (X_test, y_test),
    epochs = 5, 
)
print('Success')

print('Get accuracy ...')
_, acc = model.evaluate(X_test, y_test, verbose = 0)

print("accuracy : ", acc)
