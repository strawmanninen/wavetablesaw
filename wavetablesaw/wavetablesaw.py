#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
#
# Wavetablesaw - A wavetable manipulation tool
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>
# Licensed under MIT license, see the LICENSE file for details
#
"""
wavetablesaw.py - a wavetable manipulation tool

This is the main entry point when running from command line

See https://github.com/strawmanninen/wavetablesaw for more details

"""
import soundfile
import os.path

from arguments import get_arguments
from audioutils import wave_to_mono
from fileutils import get_files
from convert import convert_wavetable
from shuffle import shuffle_wavetable
from extract import extract_wavetable
from reverse import reverse_wavetable


def get_pattern(command: str) -> str:
    """

    Args:
        command (str): the command to get the filename pattern for

    Returns:
        (str): the pattern

    """
    patt = ""
    if command == 'convert':
        patt = args.pattern if args.pattern else args.outsize
    if command == 'shuffle':
        patt = args.pattern if args.pattern else 'shuffled'
    if command == 'extract':
        patt = args.pattern if args.pattern else 'extract'
    if command == 'reverse':
        patt = args.pattern if args.pattern else 'reverse'

    return patt


if __name__ == "__main__":

    # get_arguments will bail out if parameters are incorrect / missing
    args = get_arguments()

    files = get_files(args.files, pattern=get_pattern(args.command), outdir=args.outdir, recursive=args.recursive)
    numfiles = 0

    for file in files:

        # create directories to output file if they don't exist
        dirname = os.path.dirname(file['out'])
        if not os.path.isdir(dirname):
            if args.verbose:
                print(f"'{dirname}' doesn't exist, creating...")
            os.makedirs(dirname)

        with soundfile.SoundFile(file['in'], "rb") as wavefile:
            wavedata = wavefile.read()
            outdata = None

            if wavefile.channels > 1:
                wavedata = wave_to_mono(wavedata)

            if args.command == 'convert':
                if args.verbose:
                    print(f"Converting '{file['in']}' into '{file['out']}'... ", end="")
                if args.verbose:
                    print(f"using method: {'interpolate' if args.interpolate else 'double'}.")
                outdata = convert_wavetable(wavedata, args.insize, args.outsize, args.interpolate)

            elif args.command == 'shuffle':
                if args.verbose:
                    print(f"Shuffling '{file}' into '{file['out']}'... ", end="")
                outdata = shuffle_wavetable(wavedata, args.insize)

            elif args.command == 'extract':
                # extract is a special case, as it returns an array of data chunks
                if args.verbose:
                    print(f"Extracting '{file}'... ", end="")
                outdata = extract_wavetable(wavedata, args.insize)

            elif args.command == 'reverse':
                if args.verbose:
                    print(f"Reversing '{file}' into '{file['out']}'... ", end="")
                outdata = reverse_wavetable(wavedata, args.insize)

            with soundfile.SoundFile(
                    f"{file['out']}",
                    "wb",
                    samplerate=wavefile.samplerate,
                    channels=1,
                    subtype=wavefile.subtype,
                    format=wavefile.format,
                    endian=wavefile.endian,
            ) as outwave:
                outwave.write(outdata)
                numfiles += 1

    if args.verbose:
        print(f"Done, processed {numfiles} files.")
