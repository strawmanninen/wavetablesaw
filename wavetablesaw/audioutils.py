#
# -*- coding: utf-8 -*-
#
# Wavetablesaw - A wavetable manipulation tool
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>
# Licensed under MIT license, see the LICENSE file for details
#
"""
Utility functions for dealing with wave data
"""

import numpy as np


def wave_to_mono(data: np.array) -> np.array:
    """
    Convert a wave array to mono

    Args:
        data (np.array): stereo input data

    Returns:
        (np.array): mono output data

    """
    frames = np.shape(data)[0]
    shape = frames,
    monodata = np.zeros(shape, dtype=data.dtype)
    for i in range(frames):
        monodata[i] = data[i][0]

    return monodata


def copy_block(indata: np.array, outdata: np.array, inblock: int, outblock: int, size: int):
    """

    Args:
        indata:
        outdata:
        inblock:
        outblock:
        size:

    """

    for x in range(size):
        outdata[outblock * size + x] = indata[inblock * size + x]

    return
