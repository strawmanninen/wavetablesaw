#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>


import glob
import re
from typing import List


def glob_files(filelist: List[str]) -> List[str]:
    """Handle wildcards in input files.

    This is mainly for Windows, which doesn't do shell expansion.

    Args:
        filelist (List[str]): list of files optionally with wildcard expression

    Returns:
        List[str]: the processed list of files
    """

    globlist = []
    for f in filelist:
        # check if file contains typical wildcards
        if re.search(r"[\?\*]", f):

            for globbed in glob.glob(f):
                globlist.append(globbed)
        else:
            globlist.append(f)

    return globlist


def parse_filename(filename: str, pat: str) -> str:
    """generates output filename with pattern addition

    Args:
        filename (str): file to process
        pat (str): pattern to add

    Returns:
        str: generated filename
    """

    # very naive implementation
    idx = filename.rfind(".")

    name = filename[:idx]
    ext = filename[idx:]

    out = f"{name}-{pat}{ext}"

    return out
