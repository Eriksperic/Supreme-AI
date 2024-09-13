import numpy as np


class NetworkBuilder:

    def __init__(self):
        self.network = []


    def build_convolutional_layer(self, num_kernels, kernel_size, input_channels):


        # Det som insertas behöver kunna anropas med ett input samt returnera ett output
        # Lambda-funktion??

        num_input_units = input_channels * kernel_size * kernel_size

        # He Initialization (using normal distribution)
        norm_dist = np.sqrt(2.0 / num_input_units)
        kernels = np.random.normal(0, norm_dist, (num_kernels, input_channels, kernel_size, kernel_size))



        conv = self._convolution_algorithm

        self.network.insert(0, )




    def build_pooling_layer(self, pool_size, subsampling_op):
        pass

    # factor: how much of the info should be thrown away? (0.5 for 50%, 0,25 for 25%)
    def build_dropout_layer(self, factor):
        pass

    # Builds a fully connected (Dense) layer
    def build_dense_layer(self, neuron_count, activation_func):
        pass

    def build_flattening_layer(self):
        pass

    def build_output_layer(self, loss_func):
        pass

    def get_network(self):
        return self.network



    def _convolution_algorithm(self, input):




        return input


class Director:
    def __init__(self, builder):
        self.builder = builder
        self.layer_map = {
            'conv': self.builder.build_conv_layer,
            'pool': self.builder.build_pooling_layer,
            'flat': self.builder.build_flattening_layer,
            'dense': self.builder.build_dense_layer,
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


