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
import soundfile


def double_wavetable(data, insize, interpolate):
    """

    Args:
        data:
        insize:
        interpolate

    Returns:

    """

    datashape = np.shape(data)
    # outdata = np.empty((datashape[0] * 2, datashape[1]))
    outdata = np.empty((datashape[0] * 2, ))

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
    outdata = np.empty((datashape[0] // 2, ))

    for i in range(datashape[0] // 2):
        outdata[i] = data[i * 2]

    return outdata


def convert_wavetable(
        infile: str, outfile: str, insize: int, outsize: int, interpolate: bool, verbose=False
) -> None:
    """Handle the wavetable conversion

    Args:
        infile (str): input file name
        outfile (str): output file name
        insize (int): input period size
        outsize (int): output period size
        interpolate (bool): interpolate output (True), or use sample doubling
        verbose (bool): display output if True
    """

    with soundfile.SoundFile(infile, "rb") as wave:

        data = wave.read()
        frames = np.shape(data)[0]

        if verbose:
            print(
                f"Samplerate: {wave.samplerate} Channels:{wave.channels}" 
                "Format: {wave.format}/{wave.subtype}, Frames: {frames}"
            )

        # convert to mono
        if wave.channels > 1:
            shape = frames,
            monodata = np.zeros(shape, dtype=data.dtype)
            for i in range(frames):
                monodata[i] = data[i][0]

            data = monodata

        ratio = outsize / insize
        outdata = None

        if ratio > 1:
            outdata = double_wavetable(data, insize, interpolate)
        if ratio < 1:
            outdata = halve_wavetable(data)

        # currently we use same output format as input

        with soundfile.SoundFile(
                f"{outfile}",
                "wb",
                samplerate=wave.samplerate,
                channels=1,
                subtype=wave.subtype,
                format=wave.format,
                endian=wave.endian,
        ) as outwave:
            outwave.write(outdata)
