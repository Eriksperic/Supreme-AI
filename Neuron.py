import tensorflow as tf
import numpy as np
import math


class Neuron:

    def __init__(self, inputs, weights, bias):
        self.inputs = np.array(inputs, dtype=object)  # list of inputs -- // --
        self.weights = np.array(weights, dtype=object)  # list of weights that goes into the neuron
        self.bias = bias

    def set_weights(self, weights):
        self.weights = weights

    def calculate_output(self, activation_func):

        dot_sum = np.dot(self.inputs, self.weights) + self.bias

        return activation_func(dot_sum)


class NeuralNetwork:

    def __init__(self, layers, learning_rate):
        self.layers = layers
        self.network = []
        # create all neurons in the network

        for k in range(1, len(layers)):
            for i in range(1, layers):



class Layer:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.weights = None
        self.biases = None
        self.inputs = None
        self.outputs = None






# Somewhat like LeNet
class ConvNet(NeuralNetwork):


    # layer_config is a string containing
    # the layer configuration type c (convolutional)
    # or p (pooling)
    def __init__(self, learning_rate, layer_config="cpcp"):
        self.learning_rate = learning_rate

        self.layers = self.create_layers(layer_config)


    @staticmethod
    def create_layers(layer_config="cpcp"):
        for element in layer_config:



    @staticmethod
    def create_pooling_layer():
        return 0

    @staticmethod
    def create_convolutional_layer():
        return 0







# Place for testing

convnet = ConvNet()






