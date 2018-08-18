import tensorflow as tf

class Network:
    def __init__(self):
        """Initialzie Network Object.
        Returns:
            None.
        """
        return

    def build_network(self, var_scope=''):
        """Build network structure
        Arguments:
            var_scope: variable scope
        Returns:
            dictionary of tensors
          """
        net = {'input':{},
               'preds':{},
               'evals':{}, # Evaluaitions, e.g. confusion matrix, accuracy
               'hyper':{}, # Hyperparameters, e.g. learn rate
               'internal':{}}

        with tf.variable_scope(var_scope):
            # Initialzie variables in herere
            pass
        return net
