import tensorflow as tf

def load_data_mnist():
    """Loads MNIST dataset.
    Returns:
        Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
    """
    mnist = tf.keras.datasets.mnist
    return mnist.load_data()
