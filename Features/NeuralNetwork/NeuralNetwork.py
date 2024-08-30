from NetworkBuilder import NetworkBuilder
from NetworkBuilder import Director
from Utilities.LossFunctions import cross_entropy


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






# Somewhat like LeNet
class ConvNet(NeuralNetwork):

    builder = NetworkBuilder()
    director = Director(builder)
    config = [
        {'type': 'c', 'params': {'filters': 32, 'kernel_size': 3}},
        {'type': 'p', 'params': {'pool_size': 2}},
        {'type': 'c', 'params': {'filters': 64, 'kernel_size': 3}},
        {'type': 'p', 'params': {'pool_size': 2}},
        {'type': 'f', 'params': {}},
        {'type': 'fc', 'params': {}},
        {'type': 'o', 'params': {'loss_func': cross_entropy}},
    ]
    network = director.make_conv_neural_network(config)
    print(network)


    # layer_config is a string containing
    # the layer configuration type c (convolutional)
    # or p (pooling)
    def __init__(self, learning_rate, layer_config):
        self.learning_rate = learning_rate
        self.layers = self.create_layers(layer_config)




# Place for testing
input_image = np.array(shape=(5, 5, 3))




convnet = ConvNet(learning_rate=1)





