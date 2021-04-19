#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>
#

from arguments import get_arguments
from fileutils import get_files
from convert import convert_wavetable
from shuffle import shuffle_wavetable
from extract import extract_wavetable
from reverse import reverse_wavetable


def get_pattern(command: str) -> str:
    """

    Args:
        command:

    Returns:

    """
    patt = ""
    if args.command == 'convert':
        patt = args.pattern if args.pattern else args.outsize
    if args.command == 'shuffle':
        patt = args.pattern if args.pattern else 'shuffled'
    if args.command == 'extract':
        patt = args.pattern if args.pattern else 'extract'
    if args.command == 'reverse':
        pattern = args.pattern if args.pattern else 'reverse'

    return patt


if __name__ == "__main__":

    args = get_arguments()
    files = get_files(args.files, pattern=get_pattern(args.command), outdir=args.outdir, recursive=args.recursive)

    print(files)

    if args.command == 'convert':
        if args.verbose:
            print(f"Using method: {'interpolate' if args.interpolate else 'double'}.")

        for file in files:
            if args.verbose:
                print(f"Converting '{file}' into '{file['out']}'... ", end="")

            convert_wavetable(
                file['in'],
                file['out'],
                args.insize,
                args.outsize,
                args.interpolate,
                verbose=args.verbose,
            )
    elif args.command == 'shuffle':
        for file in files:
            if args.verbose:
                print(f"Shuffling '{file}' into '{file['out']}'... ", end="")

            shuffle_wavetable(
                file['in'],
                file['out'],
                args.insize,
                verbose=args.verbose,
            )
    elif args.command == 'extract':
        for file in files:
            if args.verbose:
                print(f"Shuffling '{file}' into '{file['out']}'... ", end="")

            extract_wavetable(
                file['in'],
                file['out'],
                args.insize,
                verbose=args.verbose,
            )
    elif args.command == 'reverse':
        for file in files:
            if args.verbose:
                print(f"Reversing '{file}' into '{file['out']}'... ", end="")

            reverse_wavetable(
                file['in'],
                file['out'],
                args.insize,
                verbose=args.verbose,
            )

    if args.verbose:
        print("Done.")
