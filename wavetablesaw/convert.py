#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>


import numpy as np
import soundfile


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
    """

    with soundfile.SoundFile(infile, "rb") as wave:

        if verbose:
            print(
                f"Samplerate: {wave.samplerate} Channels:{wave.channels} Format: {wave.format}/{wave.subtype}"
            )

        ratio = outsize / insize

        print(f"ratio {ratio}")

        data = wave.read()

        datashape = np.shape(data)
        outdata = np.empty((datashape[0] * 2, datashape[1]))

        for i in range(datashape[0]):
            outdata[i * 2] = data[i]

            if interpolate == True:
                # linear interpolation
                outdata[i * 2 + 1] = (
                    (data[i][0] + data[(i + 1) % insize][0]) / 2.0,
                    (data[i][1] + data[(i + 1) % insize][1]) / 2.0,
                )
            else:
                # double / truncate
                outdata[i * 2 + 1] = data[i]

        # TODO: add file format conversion, currently we use same as input

        # with soundfile.SoundFile(
        #     f"{outfile}",
        #     "wb",
        #     samplerate=wave.samplerate,
        #     channels=wave.channels,
        #     subtype=wave.subtype,
        #     format=wave.format,
        #     endian=wave.endian,
        # ) as outwave:
        #     outwave.write(outdata)
