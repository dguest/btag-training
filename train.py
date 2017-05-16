#!/usr/bin/env python3

"""
Example training program for b-tagging with keras
"""

import h5py
from argparse import ArgumentParser
import numpy as np

def get_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('input_file')
    return parser.parse_args()

def run():
    args = get_args()
    with h5py.File(args.input_file, 'r') as hdf_file:
        sample_jets = hdf_file['jets'][0:10]
        sample_tracks = hdf_file['tracks'][0:10,:]
    print(sample_tracks.dtype.names)
    print(sample_jets.dtype.names)

if __name__ == '__main__':
    run()
