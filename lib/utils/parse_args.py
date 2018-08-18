import argparse

def parse_args ():
    """Initialzie Argument Parsers Object.
        Returns:
            Parser object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default='input', help='Path to input directory')
    parser.add_argument('-o', '--output', default='output', help='Path to output directory')
    args = parser.parse_args()
    return args