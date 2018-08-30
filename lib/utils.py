import argparse, pickle
import numpy as np
import tensorflow as tf

def parse_args ():
    """Initialzie Argument Parsers Object.
        Returns:
            parser object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default='input', help='Path to input directory')
    parser.add_argument('-o', '--output', default='output', help='Path to output directory')
    args = parser.parse_args()
    return args


def dump_pickle(path, result):
    """Saves result to a .pkl file
        Arguments:
            path: path to save pickle file
            result: object to be saved
    """
    if not path.endswith(".pkl"):
        path += ".pkl"
    with open(path, "wb") as f:
        pickle.dump(result, f)


def load_pickle(path):
    """Load result from a .pkl file
        Arguments:
            path: path to save pickle file
        Returns:
            result loaded from pickle file
    """
    if not path.endswith(".pkl"):
        raise Exception("Invalid Argument: path must be a .pkl file")
    with open(path, "rb") as f:
        result = pickle.load(f)
    return result


def fancy_print(obj, indent=0):
    """Structurally print the object given
        Arguments:
            obj: the object to be printed
            indent: the current indentation level
    """
    if isinstance(obj, (str, int)):
        print(indent*' ', obj)
    elif isinstance(obj, float):
        print(indent*' ', '%.3f'%obj)
    elif isinstance(obj, np.ndarray):
        print(indent*' ', 'np '+str(obj.shape))
    elif isinstance(obj, tf.Tensor):
        print(indent*' ', str(obj.shape))
    elif isinstance(obj, (list, tuple, set)):
        print(indent*' ', type(obj))
        for item in obj:
            fancy_print(item, indent+4)
        print(indent*' ', "END")
    elif isinstance(obj, dict):
        print(indent*' ', type(obj))
        for key, val in obj.items():
            print((indent+2)*' ', key)
            fancy_print(val, indent+4)
        print(indent*' ', "END")
    else:
        raise Exception("Type %s not supported."%type(obj))


if __name__ == '__main__':
    test_obj = {1:{'2':0.12341241,0.1232131:'345',(1,2,3):'lineA'}, 'cars':[{'pos1':1,'pos2':2, 'fc':np.array([[1,2],[3,4]])}, {'pos1':0,'pos2':0, 'fc':np.array([[0,3],[2,1]])}]}
    fancy_print(test_obj)
