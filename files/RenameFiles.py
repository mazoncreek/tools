#!/usr/bin/python
#
#   Rename files with a pattern
#

# ==========================================================================

import argparse
import glob
import os
import time

# ==========================================================================


def main():
    parser = argparse.ArgumentParser(description="Rename Files")
    parser.add_argument("InputFileMask", action="store", help="Input File Name")
    parser.add_argument("OutputFileStub", action="store", help="Output File Name")
    parser.add_argument("--Verbose", action="store_true", default=False, help="Verbose Operation")
    parser.add_argument("--Write", action="store_true", default=False, help="Write Output")

    args = parser.parse_args()

    input_filename_mask = args.InputFileMask
    output_filename_stub = args.OutputFileStub

    verbose = args.Verbose
    write = args.Write

    filename_list = sorted(glob.glob(input_filename_mask))

    for filename in filename_list:
        print(f"processing {filename}")
        fields = filename.split("-")

        if len(fields) == 1:
            if verbose:
                print(f"Skipping {filename}")
            continue

        output_filename = output_filename_stub
        for field in fields[1:]:
            output_filename = output_filename + "-" + field

        if verbose:
            print(f"Copying to {output_filename}")

        if write:
            os.system(f"cp \"{filename}\" \"{output_filename}\"")
            os.system(f"touch \"{output_filename}\"")
            time.sleep(1)

    return


# ==========================================================================


if __name__ == "__main__":
    main()
