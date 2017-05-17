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

def flatten(ds):
    ftype = [(n, float) for n in ds.dtype.names]
    flat = ds.astype(ftype).view(float).reshape(ds.shape + (-1,))
    return flat.swapaxes(1, len(ds.shape))

def run():
    args = get_args()
    with h5py.File(args.input_file, 'r') as hdf_file:
        sample_jets = hdf_file['jets'][0:3]
        sample_tracks = hdf_file['tracks'][0:3,:]

    print(flatten(sample_jets[['pt', 'eta']]))
    print(flatten(sample_tracks[['pt','numberOfPixelHits']]))


if __name__ == '__main__':
    run()
