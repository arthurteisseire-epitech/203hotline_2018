import sys
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    if len(sys.argv) == 2:
        parser.add_argument('d', type=int)
    elif len(sys.argv) == 3:
        parser.add_argument('n', type=int)
        parser.add_argument('k', type=int)
    return parser.parse_args()
