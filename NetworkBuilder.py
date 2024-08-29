import numpy as np


class NetworkBuilder:

    def __init__(self):
        self.network = []


    def build_convolutional_layer(self, filters, kernel_size):
        pass

    def build_pooling_layer(self, pool_size, subsampling_op):
        pass

    # Builds a fully connected layer
    def build_FC_layer(self, neuron_count, activation_func):
        pass

    def build_flattening_layer(self):
        pass

    def build_output_layer(self, loss_func):
        pass

    def get_network(self):
        pass


class Director:
    def __init__(self, builder):
        self.builder = builder
        self.layer_map = {
            'c': self.builder.build_conv_layer,
            'p': self.builder.build_pooling_layer,
            'f': self.builder.build_flattening_layer,
            'fc': self.builder.build_FC_layer,
            'o': self.builder.build_output_layer
        }
    def make_conv_neural_network(self, config):
        for layer_config in config:
            layer_type = layer_config['type']
            params = layer_config.get('params', {})
            if layer_type in self.layer_map:
                self.layer_map[layer_type](**params)
            else:
                raise ValueError(f"Invalid layer type: {layer_type}")
        return self.builder.get_network()


