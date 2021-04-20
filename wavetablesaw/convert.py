#
# -*- coding: utf-8 -*-
#
# Wavetablesaw - A wavetable manipulation tool
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>
# Licensed under MIT license, see the LICENSE file for details
#
"""
Handles wave table period size conversion
"""

import numpy as np


def double_wavetable(data: np.array, insize: int, interpolate: bool):
    """

    Args:
        data:
        insize:
        interpolate

    Returns:

    """

    datashape = np.shape(data)
    # outdata = np.empty((datashape[0] * 2, datashape[1]))
    outdata = np.empty((datashape[0] * 2,))

    for i in range(datashape[0]):
        outdata[i * 2] = data[i]

        if interpolate:
            # linear interpolation
            outdata[i * 2 + 1] = (
                    (data[i] + data[(i + 1) % insize]) / 2.0
            )
        else:
            # double / truncate
            outdata[i * 2 + 1] = data[i]

    return outdata


def halve_wavetable(data) -> np.array:
    """

    Args:
        data (np.array): input wave data to process

    Returns:
        (np.array) halved wavetable data

    """
    datashape = np.shape(data)
    outdata = np.empty((datashape[0] // 2,))

    for i in range(datashape[0] // 2):
        outdata[i] = data[i * 2]

    return outdata


def convert_wavetable(data: np.array, insize: int, outsize: int, interpolate: bool) -> np.array:
    """Handle the wavetable conversion

    Args:
        data (np.array): input wavetable data
        insize (int): input period size
        outsize (int): output period size
        interpolate (bool): interpolate output (True), or use sample doubling

    Returns:
        (np.array): the converted wavetable
    """

    ratio = outsize / insize
    outdata = None

    if ratio > 1:
        outdata = double_wavetable(data, insize, interpolate)
    if ratio < 1:
        outdata = halve_wavetable(data)

    return outdata
