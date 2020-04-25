import numpy as np
import tensorflow  as tf


if __name__ == "__main__":
    data = np.loadtxt('assets/data1.csv', delimiter=',')

    x_train = data[:,0:2]
    y_train = data[:,2]

    model = tf.keras.models.Sequential(
        tf.keras.layers.Dense(1, activation='sigmoid')
    )

    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    model.fit(x_train, y_train, epochs=1000)
