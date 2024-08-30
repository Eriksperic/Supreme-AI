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




