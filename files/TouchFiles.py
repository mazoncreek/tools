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
    parser = argparse.ArgumentParser(description="Touch Files")
    parser.add_argument("InputFileMask", action="store", help="Input File Name")
    parser.add_argument("--Verbose", action="store_true", default=False, help="Verbose Operation")

    args = parser.parse_args()

    input_filename_mask = args.InputFileMask

    verbose = args.Verbose

    filename_list = sorted(glob.glob(input_filename_mask))

    for filename in filename_list:
        print(f"processing {filename}")

        os.system(f"touch \"{filename}\"")
        time.sleep(1)

    return


# ==========================================================================


if __name__ == "__main__":
    main()
