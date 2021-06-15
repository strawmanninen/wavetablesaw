# Wavetablesaw

A wavetable conversion and manipulation tool, 
enables adjusting the wavetable size and other things.

    usage: wavetablesaw.py [-h] [-v] [-r] [-out [outdir]] {convert,shuffle,extract,reverse} ...

    Manipulate wavetable files

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         verbose operation
      -r, --recursive       recurse input directories
      -out [outdir], --outdir [outdir]
                            output files to specified directory

    command:
      the operation to run

      {convert,shuffle,extract,reverse}
                            command
        convert             convert wavetable size
        shuffle             shuffle wavetable
        extract             extract individual slices of a wavetable
        reverse             reverse wavetablse

    run with commandname -h for help with a particular command
