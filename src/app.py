import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

from src.network import DeepNeuralNetwork
from src.process import ProcessImage


class Application (object):

    def __init__(self, args):
        self.args = args

    def loadConfig(self):

        with open('data/config.json') as data_file:
            data = json.load(data_file)

        return data

    def run(self):
        print("@--------------------| Inciando Leitura dataset |--------------------------@")
        ProcessImage.loadDataset(self.args['dataset'])

        print("@--------------------|      Inciando Keras             |--------------------------@")

        net = DeepNeuralNetwork([], [])

        print("@--------------------| Inciando Deep Deural Networking |------------------------@")
