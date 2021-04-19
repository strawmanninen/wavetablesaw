#
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Straw Manninen <strawmanninen@outlook.com>
#

from pathlib import Path
import os
import os.path
from typing import List, Dict


def get_files(filelist: List[str], pattern='', outdir: str = '', recursive: bool = False) -> List[Dict]:
    """

    Args:
        filelist (List[str]): List of files or wildcards
        pattern (str): pattern to append to the output filename
        outdir (str): output directory if not same as input
        recursive (bool): recurse directories

    Returns:
        (List[Dict]): a dictionary of input/output filenames

    """

    globlist = []

    # NB: this code is pretty hairy at the moment and could be clarified quite a bit

    for file in filelist:
        parts = Path(file).parts
        # if we're dealing with an ordinary file, create the in/out dictionary optionally adjusting the output directory
        if os.path.isfile(file):
            indir = parts[0]
            infile = os.sep.join(parts[1:])
            outfile = parse_filename(outdir + os.sep + infile if outdir else indir + os.sep + infile, pattern)
            globlist.append({'in': file, 'out': outfile})
        # else do a glob, recursive if defined
        elif "*" in parts[-1]:
            glob = parts[-1]
            indir = os.sep.join(parts[0:-1])
            paths = Path(indir).glob(glob)

            if recursive:
                paths = Path(indir).rglob(glob)

            for path in paths:
                if os.path.isfile(path):
                    file = os.sep.join(path.parts[1:])
                    outfile = parse_filename(outdir + os.sep + file if outdir else file, pattern)
                    globlist.append({'in': os.sep.join(path.parts), 'out': outfile})

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
