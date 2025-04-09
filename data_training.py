import os
import numpy as np
import cv2
from tensorflow.keras.utils import to_categorical

from tf.keras import Input, Dense
from tf.keras import Model

# Create the model and make changes for compatibility
model = tf.keras.Sequential([
  tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
  tf.keras.layers.MaxPooling2D((2, 2)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(64, activation='relu'),
  tf.keras.layers.Dense(10)
])

# Save the model using the native module
model.save("model.h5")

# Save the labels using numpy.save
np.save("labels.npy", np.array(label))