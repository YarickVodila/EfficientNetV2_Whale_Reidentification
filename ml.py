import cv2
import keras
import numpy as np
import tensorflow as tf


def SSIMLoss(y_true, y_pred):
    return 1 - tf.reduce_mean(tf.image.ssim(y_true, y_pred, 1.0))


optimizer = tf.keras.optimizers.Adam(lr=0.0005)
autoencoder = keras.models.load_model('autoencoder.h5', compile=False)
autoencoder.compile(optimizer=optimizer, loss=SSIMLoss)
model = keras.models.load_model('EffNetb0v2_ep30.h5')


def _is_unknown_whale(pred, image_test):
    if float(SSIMLoss(pred[0], image_test)) > 0.1:
        return True, float(SSIMLoss(pred[0], image_test))
    else:
        return False, float(SSIMLoss(pred[0], image_test))


def is_unknown_whale(image):
    pred = autoencoder.predict(np.array(image))
    return _is_unknown_whale(pred, image)


def get_top(image, top=5):
    image = cv2.imread(image)
    image = [cv2.resize(image, (224, 224))]
    image = np.array(image).astype('float32') / 255.0
    pred = model.predict(image)
    pred_sorted = [(list(pred[0]).index(x)) for x in sorted(list(pred[0]))[-top:]]
    top = list(reversed(pred_sorted))
    anti = is_unknown_whale(image)[0]
    if anti:
        top[0] = -1
    return top
