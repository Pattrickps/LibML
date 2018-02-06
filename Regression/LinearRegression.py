import numpy as np

class LinearRegression:
    def __init__(self):
        self.b = None # Weights numpy array [ Updated during training ]
        self.x = np.zeros((100, 10)) # Default shape of 100 x 10 [ 100 rows and 10 features ]
        self.y = np.zeros((100)) # Default shape of 100 [ 100 labels]
        print("Initialized x array of shape: {0} and y array of shape: {1}".format(self.x.shape, self.y.shape))

    def train(self, x, y):
        """

        :param x: Numpy array of features
        :param y: Numpy array of labels
        :return: None
        """

    def evaluate(self, x):
        """

        :param x: Numpy array of features
        :return: Numpy array of predicted labels
        """


def gradient_descent_iteration(b, x, y):
    """

    :param b: Weights numpy array
    :param x: Features numpy array
    :param y: Labels numpy array
    :return: Weights numpy array
    """

if __name__ == "__main__":
    lr_instance = LinearRegression()
    print("Linear Regression Model Class")
