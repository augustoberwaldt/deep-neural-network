# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt



class Application:

    def loadConfig(self):
        with open('data/config.json') as data_file:
            data = json.load(data_file)

        return data

    def run(self):
        
        
        print("@--------------------| Inciando Leitura dataset |--------------------------@")

        print("@--------------------| Inciando Keras |--------------------------@")
        print(tf.__version__)
        print("@--------------------| Inciando Deep Deural Networking |------------------------@")
