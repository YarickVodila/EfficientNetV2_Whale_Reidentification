import cv2
from tensorflow import keras
import numpy as np
import tensorflow as tf


def SSIMLoss(y_true, y_pred):
    return 1 - tf.reduce_mean(tf.image.ssim(y_true, y_pred, 1.0))


optimizer = tf.keras.optimizers.Adam(lr=0.0005)
autoencoder = keras.models.load_model('autoencoder.h5', compile=False)
autoencoder.compile(optimizer=optimizer, loss=SSIMLoss)
model = keras.models.load_model('model.h5')


def _is_unknown_whale(pred, image_test):
    if float(SSIMLoss(pred[0], image_test)) > 0.035:
        return True, float(SSIMLoss(pred[0], image_test))
    else:
        return False, float(SSIMLoss(pred[0], image_test))


def is_unknown_whale(image):
    pred = autoencoder.predict(np.array(image))
    result = _is_unknown_whale(pred, image)
    return result


def resized(image, x, y):
    image = [cv2.resize(image, (x, y))]
    image = np.array(image).astype('float32') / 255.0
    return image


def get_top(image, top=5):
    image = cv2.imread(image)
    pred = model.predict(resized(image, 240, 240))
    pred_sorted = [(list(pred[0]).index(x) + 1) for x in sorted(list(pred[0]))[-top:]]
    top = list(reversed(pred_sorted))
    is_unknown = is_unknown_whale(resized(image, 224, 224))[0]
    if is_unknown:
        top[0] = 0
    return top
