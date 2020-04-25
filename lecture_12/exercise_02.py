import numpy as np
import tensorflow as tf


if __name__ == "__main__":
    train = np.loadtxt('assets/train.csv', delimiter=',')
    x_train = train[:,0:2]
    y_train = train[:,2]

    test = np.loadtxt('assets/test.csv', delimiter=',')
    x_test = train[:,0:2]
    y_test = train[:,2]

    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(10, activation = 'relu'),
        tf.keras.layers.Dense(10, activation = 'relu'),
        tf.keras.layers.Dense(10, activation = 'relu'),
        tf.keras.layers.Dense(1, activation = 'sigmoid'),
    ])

    model.compile(
        optimizer = 'adam',
        loss = 'binary_crossentropy',
        metrics = ['accuracy']
    )

    result = model.fit(x_train, y_train, epochs = 100, validation_data = (x_test, y_test))
    model.evaluate(x_test, y_test)
    np.savetxt('./result_02.csv', result.history['val_accuracy'], delimiter=',')
