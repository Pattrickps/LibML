import numpy as np
from utils.verbose_utils import describe_class, describe_function
import pandas as pd

class LinearRegression:
    def __init__(self, n_iterations=1000):
        describe_class(self)
        self.iterations = n_iterations
        self.b = None # Weights numpy array [ Updated during training ]
        self.x = np.zeros((100, 10)) # Default shape of 100 x 10 [ 100 rows and 10 features ]
        self.y = np.zeros((100)) # Default shape of 100 [ 100 labels]
        describe_function(self, "shape", ["x", "y"])
        describe_function(self, None, ["b"])

    def train(self, x, y):
        """

        :param x: Numpy array of features
        :param y: Numpy array of labels
        :return: None
        """
        b = np.zeros(x.shape[1] + 1)
        # for i in range(x.shape[1]):
        #     x[:][i] = 1 x[:][i]

        costs = []
        b_values = []
        for i in range(self.iterations):

            b = gradient_descent_iteration(b, x, y)
            costs.append(get_cost(x, y, b))
            b_values.append(b)
            print "Iteration: " + str(i) + " Cost: " + str(costs[i])
        self.b = b_values[costs.index(min(costs))]

    def evaluate(self, x):
        """

        :param x: Numpy array of features
        :return: Numpy array of predicted labels
        """
        y_val = []
        for x_val in range(x.shape[0]):
            y_val.append(self.b[0] + np.dot(x_val, self.b[1:]))

        return np.array(y_val)


def get_cost(x, y, b):
    """

    :param x: Numpy array of features
    :param y: Numpy array of labels
    :param b: Numpy array of weights
    :return: Cost function scalar
    """
    cost = 0
    for x_val, y_val in zip(x, y):
        cost += (b[0] + np.dot(x_val, b[1:]) - y_val) ** 2

    cost = cost / x.shape[1]
    return cost


def gradient_descent_iteration(b, x, y):
    """

    :param b: Weights numpy array
    :param x: Features numpy array
    :param y: Labels numpy array
    :return: Weights numpy array
    """
    for i, b_val in enumerate(b):
        derivative = 0
        for x_val, y_val in zip(x, y):
            if i == 0:
                derivative += (b[0] + np.dot(x_val, b[1:]) - y_val)
            else:
                derivative += (b[0] + np.dot(x_val, b[1:]) - y_val) * x_val[i - 1]
        derivative = derivative / x.shape[0]

        b[i] = b[i] - derivative

    return b

if __name__ == "__main__":
    lr_instance = LinearRegression()
    X_train = np.random.rand(100, 10)
    Y_train = np.random.rand(100)

    X_test = np.random.rand(10, 10)
    print "Shapes",; print X_train.shape, Y_train.shape
    lr_instance.train(X_train, Y_train)
    print lr_instance.evaluate(X_test)
    print("Linear Regression Model Class")
