#
# -*- coding: utf-8 -*-
#
# Wavetablesaw - A wavetable manipulation tool
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>
# Licensed under MIT license, see the LICENSE file for details
#
"""
Extract individual cycles from a wavetable
"""

import numpy as np

from audioutils import copy_block


def extract_wavetable(data: np.array, insize: int) -> [np.array]:
    """

    Args:
        data (np.array): input data
        insize (int): wavetable period size

    Returns:
        ([np.array]): an array of extracted waveforms
    """

    frames = data.shape[0]
    numcycles = int(frames / insize)

    cycles = list(range(numcycles))

    extracted = []
    for x in cycles:
        outdata = np.zeros((insize,), dtype=data.dtype)
        copy_block(data, outdata, x, 0, insize)
        extracted.append(outdata)

    return extracted

    pass
