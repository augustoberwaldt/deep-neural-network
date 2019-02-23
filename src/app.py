# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras


import numpy as np
import matplotlib.pyplot as plt
import cv2
from src.network import DeepNeuralNetwork  


class Application:

    def loadConfig(self):
        with open('data/config.json') as data_file:
            data = json.load(data_file)

        return data

    def run(self):
         
        net = DeepNeuralNetwork()         
        
        print("@--------------------| Inciando Leitura dataset |--------------------------@")
        
        img = cv2.imread('data/test.png', 0)  
        
        print(img)
        print(net)

        print("@--------------------|      Inciando Keras             |--------------------------@")
        
        print("@--------------------| Inciando Deep Deural Networking |------------------------@")
