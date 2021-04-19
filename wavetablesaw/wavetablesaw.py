#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>
#

from arguments import get_arguments
from fileutils import glob_files, parse_filename
from convert import convert_wavetable
from shuffle import shuffle_wavetable
from extract import extract_wavetable
from reverse import reverse_wavetable

if __name__ == "__main__":

    args = get_arguments()

    files = glob_files(args.files)

    if args.command == 'convert':
        pattern = args.pattern if args.pattern else args.outsize

        if args.verbose:
            print(f"Using method: {'interpolate' if args.interpolate else 'double'}.")

        for file in files:
            outfile = parse_filename(file, pattern)
            if args.verbose:
                print(f"Converting '{file}' into '{outfile}'... ", end="")

            convert_wavetable(
                file,
                outfile,
                args.insize,
                args.outsize,
                args.interpolate,
                verbose=args.verbose,
            )
    elif args.command == 'shuffle':
        pattern = args.pattern if args.pattern else 'shuffled'

        for file in files:
            outfile = parse_filename(file, pattern)
            if args.verbose:
                print(f"Shuffling '{file}' into '{outfile}'... ", end="")

            shuffle_wavetable(
                file,
                outfile,
                args.insize,
                verbose=args.verbose,
            )
    elif args.command == 'extract':
        pattern = args.pattern if args.pattern else 'extract'

        for file in files:
            outfile = parse_filename(file, pattern)
            if args.verbose:
                print(f"Shuffling '{file}' into '{outfile}'... ", end="")

            extract_wavetable(
                file,
                outfile,
                args.insize,
                verbose=args.verbose,
            )
    elif args.command == 'reverse':
        pattern = args.pattern if args.pattern else 'reverse'

        for file in files:
            outfile = parse_filename(file, pattern)
            if args.verbose:
                print(f"Reversing '{file}' into '{outfile}'... ", end="")

            reverse_wavetable(
                file,
                outfile,
                args.insize,
                verbose=args.verbose,
            )

    if args.verbose:
        print("Done.")
