#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>


from convert import convert_wavetable
from arguments import get_arguments
from fileutils import glob_files, parse_filename

if __name__ == "__main__":

    args = get_arguments()

    # handle default pattern
    pattern = args.pattern if args.pattern else args.outsize

    if args.verbose:
        print(f"Using method: {'interpolate' if args.interpolate else 'double'}.")

    files = glob_files(args.files)

    for file in files:
        outfile = parse_filename(file, pattern)
        if args.verbose:
            print(f"Processing '{file}' into '{outfile}'... ", end="")

        convert_wavetable(
            file,
            outfile,
            args.insize,
            args.outsize,
            args.interpolate,
            verbose=args.verbose,
        )

    if args.verbose:
        print("Done.")
