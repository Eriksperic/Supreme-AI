from NetworkBuilder import NetworkBuilder
from NetworkBuilder import Director
from Utilities.LossFunctions import cross_entropy
from Utilities.ActivationFunctions import *
from Utilities.SubSamplingOperations import *

import numpy as np
class NeuralNetwork:

    def __init__(self, layers, learning_rate):
        self.layers = layers
        self.network = []


class Layer:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.weights = None
        self.biases = None
        self.inputs = None
        self.outputs = None


config = [
    {'type': 'conv', 'params': {'filters': 32, 'kernel_size': 3}},
    {'type': 'pool', 'params': {'pool_size': 2}},
    {'type': 'conv', 'params': {'filters': 64, 'kernel_size': 3}},
    {'type': 'pool', 'params': {'pool_size': 2}, 'subsampling_op': max_pool},
    {'type': 'flat', 'params': {}},
    {'type': 'dense', 'params': {'activation_func': relu}},
    {'type': 'output', 'params': {'loss_func': cross_entropy}},
    ]

# Somewhat like LeNet
class ConvNet(NeuralNetwork):
    # Train for x number of Epochs
    # A x_train, y_train   (training set)
    # + x_test,  y_test     (validation set)
    # Shuffle = True (randomize the training batch order)

    def __init__(self, learning_rate, layer_config):
        self.learning_rate = learning_rate

        self.builder = NetworkBuilder()
        self.director = Director(self.builder)
        self.network = self.director.make_conv_neural_network(layer_config)


    def train_network(self, EPOCHS, Training_Data):

        for e in range(0, EPOCHS):
            # Init total training and validation loss
            total_train_loss = 0
            totalValLoss = 0

            # init the number of correct predictions in the training and validation step
            train_correct = 0
            validation_correct = 0

            # loop over training set (x =
            for (x, y) in Training_Data:

                # Forward pass and calculate training loss
                self.run_network(Training_Data)

    def run_network(self, input, layer_index=0):
        if len(self.network) == layer_index + 1:
            return input # The final output
        output = self.network[layer_index](input)
        self.run_network(output, layer_index + 1)






# Place for testing
input_image = np.array(shape=(5, 5, 3))
convnet = ConvNet(learning_rate=1, layer_config=config)


# Todo: Implement device selection (cuda / cpu)
