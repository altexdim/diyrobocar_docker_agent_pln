#!/usr/bin/env python3
"""
Scripts to convert h5 to tflite model.
Basic usage should feel familiar: convert.py --h5=model.h5 --tflite=model.tflite

Usage:
    convert.py (--h5=model.h5) (--tflite=model.tflite)
"""

from docopt import docopt
import tensorflow as tf

def main():
    args = docopt(__doc__)
    model_h5 = args['--h5']
    model_tflite = args['--tflite']

    model = tf.keras.models.load_model(model_h5)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    open(model_tflite, "wb").write(tflite_model)

if __name__ == "__main__":
    main()
