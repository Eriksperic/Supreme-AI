import numpy as np


# label_vec contains the true values
# class_vec is the predicted values after softmax has been applied
def cross_entropy(label_vec, class_vec):
    return -np.sum(label_vec * np.log(class_vec))