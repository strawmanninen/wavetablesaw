#
# -*- coding: utf-8 -*-
#
# Wavetablesaw - A wavetable manipulation tool
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>
# Licensed under MIT license, see the LICENSE file for details
#
"""
Randomize cycles in a wavetable
"""

import numpy as np
import random
from audioutils import copy_block


def shuffle_wavetable(data: np.array, insize: int):
    """
    Randomizes a wavetable

    Args:
        data (np.array): input waveform data
        insize (int): wavetable period size

    Returns:
        (np.array): The randomized wavetable
    """

    frames = data.shape[0]
    outdata = np.zeros(data.shape, dtype=data.dtype)

    numcycles = int(frames / insize)

    cycles = list(range(numcycles))
    randcycles = list(range(numcycles - 1, -1, -1))
    random.shuffle(randcycles)

    for x in cycles:
        copy_block(data, outdata, x, randcycles[x], insize)

    return outdata
