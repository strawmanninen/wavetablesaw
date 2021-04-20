#
# -*- coding: utf-8 -*-
#
# Wavetablesaw - A wavetable manipulation tool
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>
# Licensed under MIT license, see the LICENSE file for details
#
"""
Reverse a wavetable
"""

import numpy as np
from audioutils import copy_block


def reverse_wavetable(data: np.array, insize: int) -> np.array:
    """
    Reverses a wavetable

    Args:
        data (np.array): input waveform data
        insize (int): wavetable period size

    Returns:
        (np.array): The reversed wavetable
    """

    frames = data.shape[0]
    outdata = np.zeros(data.shape, dtype=data.dtype)

    numcycles = int(frames / insize)

    print(f"number of cycles to reverse: {numcycles}")

    cycles = list(range(numcycles))
    revcycles = list(range(numcycles - 1, -1, -1))

    for x in cycles:
        copy_block(data, outdata, x, revcycles[x], insize)

    return outdata
