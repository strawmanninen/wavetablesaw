# Wavetablesaw

A wavetable conversion and manipulation tool, 
enables adjusting the wavetable size and other things.

Work in progress. 
    
    usage: wavetablesaw.py [-h] [-v] [-d] [-p [pattern]] [-i [insize]] [-o [outsize]] file [file ...]
    
    Manipulate wavetable files
    
    positional arguments:
      file                  file(s) to process
    
    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         verbose operation
      -d, --double          use doubling method (default: interpolate)
      -p [pattern], --pattern [pattern]
                            pattern to append to output filename (default: output period size)
      -i [insize], --insize [insize]
                            input wavetable period size (default: 1024)
      -o [outsize], --outsize [outsize]
                            output wavetable period size (default: 2048)