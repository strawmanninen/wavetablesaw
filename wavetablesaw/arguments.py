#
# -*- coding: utf-8 -*-
#
# Wavetablesaw - A wavetable manipulation tool
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>
# Licensed under MIT license, see the LICENSE file for details
#
"""
Define command line arguments, print help/usage if called without arguments
"""

import sys
import argparse


def get_arguments() -> argparse.Namespace:
    """parse command line arguments, print help and set defaults if needed

    Returns:
        argparse.Namespace: parsed arguments
    """

    # the main parser

    parser = argparse.ArgumentParser(description="Manipulate wavetable files",
                                     epilog="run with commandname -h for help with a particular command")

    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_const",
        const=True,
        default=False,
        help="verbose operation",
    )

    parser.add_argument(
        "-r",
        "--recursive",
        dest="recursive",
        action="store_const",
        const=True,
        default=False,
        help="recurse input directories",
    )

    parser.add_argument(
        "-out",
        "--outdir",
        metavar="outdir",
        type=str,
        const="outdir",
        default="",
        nargs="?",
        help="output files to specified directory",
        required=False,
    )

    # parsers for the individual commands

    cmdparsers = parser.add_subparsers(title="command", description="the operation to run", help="command",
                                       dest="command", required=True)

    convert_parser = cmdparsers.add_parser('convert', help="convert wavetable size")
    shuffle_parser = cmdparsers.add_parser('shuffle', help="shuffle wavetable")
    extract_parser = cmdparsers.add_parser('extract', help="extract individual slices of a wavetable")
    reverse_parser = cmdparsers.add_parser('reverse', help="reverse wavetablse")

    # arguments for conversion

    convert_parser.add_argument(
        "files",
        metavar="file",
        type=str,
        nargs="+",
        help="file(s) to process",
    )

    convert_parser.add_argument(
        "-d",
        "--double",
        dest="interpolate",
        action="store_const",
        const=False,
        default=True,
        help="use doubling method (default: interpolate)",
    )

    convert_parser.add_argument(
        "-p",
        "--pattern",
        metavar="pattern",
        type=str,
        const="pattern",
        default="",
        nargs="?",
        help="pattern to append to output filename (default: output period size)",
        required=False,
    )

    convert_parser.add_argument(
        "-i",
        "--insize",
        metavar="insize",
        type=int,
        const="insize",
        default=1024,
        choices=[512, 1024, 2048],
        nargs="?",
        help="input wavetable period size (default: 1024)",
        required=False,
    )

    convert_parser.add_argument(
        "-o",
        "--outsize",
        metavar="outsize",
        type=int,
        const="outsize",
        default=2048,
        choices=[512, 1024, 2048],
        nargs="?",
        help="output wavetable period size (default: 2048)",
        required=False,
    )

    # arguments for shuffling

    shuffle_parser.add_argument(
        "files",
        metavar="file",
        type=str,
        nargs="+",
        help="file(s) to process",
    )

    shuffle_parser.add_argument(
        "-p",
        "--pattern",
        metavar="pattern",
        type=str,
        const="pattern",
        default="",
        nargs="?",
        help="pattern to append to output filename (default: 'shuffled')",
        required=False,
    )

    shuffle_parser.add_argument(
        "-i",
        "--insize",
        metavar="insize",
        type=int,
        const="insize",
        default=1024,
        choices=[512, 1024, 2048],
        nargs="?",
        help="input wavetable period size (default: 1024)",
        required=False,
    )

    shuffle_parser.add_argument(
        "-o",
        "--outsize",
        metavar="outsize",
        type=int,
        const="outsize",
        default=2048,
        choices=[512, 1024, 2048],
        nargs="?",
        help="output wavetable period size (default: 2048)",
        required=False,
    )

    # arguments for extraction

    extract_parser.add_argument(
        "files",
        metavar="file",
        type=str,
        nargs="+",
        help="file(s) to process",
    )

    extract_parser.add_argument(
        "-p",
        "--pattern",
        metavar="pattern",
        type=str,
        const="pattern",
        default="",
        nargs="?",
        help="pattern to append to output filename (default: 'extract'+number of slice)",
        required=False,
    )

    extract_parser.add_argument(
        "-i",
        "--insize",
        metavar="insize",
        type=int,
        const="insize",
        default=1024,
        choices=[512, 1024, 2048],
        nargs="?",
        help="input wavetable period size (default: 1024)",
        required=False,
    )

    # arguments for reversing

    reverse_parser.add_argument(
        "files",
        metavar="file",
        type=str,
        nargs="+",
        help="file(s) to process",
    )

    reverse_parser.add_argument(
        "-p",
        "--pattern",
        metavar="pattern",
        type=str,
        const="pattern",
        default="",
        nargs="?",
        help="pattern to append to output filename (default: 'reverse')",
        required=False,
    )

    reverse_parser.add_argument(
        "-i",
        "--insize",
        metavar="insize",
        type=int,
        const="insize",
        default=1024,
        choices=[512, 1024, 2048],
        nargs="?",
        help="input wavetable period size (default: 1024)",
        required=False,
    )

    if len(sys.argv) == 1:
        parser.print_usage()
        print(f"run '{sys.argv[0]} -h' for detailed usage")
        sys.exit(1)

    return parser.parse_args()
