#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>


import argparse


def get_arguments() -> argparse.Namespace:
    """parse command line arguments, print help and set defaults if needed

    Returns:
        argparse.Namespace: parsed arguments
    """

    parser = argparse.ArgumentParser(description="Change wavetable file periods.")

    parser.add_argument(
        "files",
        metavar="file",
        type=str,
        nargs="+",
        help="file(s) to process",
    )

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
        "-d",
        "--double",
        dest="interpolate",
        action="store_const",
        const=False,
        default=True,
        help="use doubling method (default: interpolate)",
    )

    parser.add_argument(
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

    parser.add_argument(
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

    parser.add_argument(
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

    return parser.parse_args()
