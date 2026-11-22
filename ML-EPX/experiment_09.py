import tensorflow as tf
from tensorflow.keras import layers, models

# Makes the random initialisation and training setup reproducible.
tf.keras.utils.set_random_seed(7)

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

model = models.Sequential([
    layers.Input(shape=(28, 28)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(X_train, y_train, epochs=1, batch_size=128, verbose=0)

print('MNIST training completed.')
print('Input shape:', model.input_shape)
print('Output classes:', model.output_shape[-1])
