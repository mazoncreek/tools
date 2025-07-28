#!/usr/bin/python
#
#   Rename Joplin PDF files with a consistent number
#

# ==========================================================================

import argparse
import glob
import os

# ==========================================================================


def main():
    parser = argparse.ArgumentParser(description="Rename Joplin PDF files")
    parser.add_argument("InputFiles", action="store", help="Input File Names")
    parser.add_argument("--OutputDirectory", action="store", default=".", help="Output Directory")
    parser.add_argument("--Verbose", action="store_true", default=False, help="Verbose Operation")
    parser.add_argument("--Write", action="store_true", default=False, help="Write Output")
    parser.add_argument("--Rename", action="store_true", default=False, help="Rename Files")

    args = parser.parse_args()

    input_filenames = args.InputFiles
    output_directory = args.OutputDirectory

    verbose = args.Verbose
    write = args.Write
    rename = args.Rename
    command = "mv" if rename else "cp"

    filename_list = sorted(glob.glob(input_filenames))

    for filename in filename_list:
        print(f"processing {filename}")
        processed_filename = cleanup_filename(filename)
        fields = processed_filename.split("_")
        print(fields)
        continue

        if len(fields) == 1:
            if verbose:
                print(f"Skipping {filename}")
            continue

        output_filename = output_directory
        for field in fields[1:]:
            output_filename = output_filename + "-" + field

        if verbose:
            print(f"Ouput filename {output_filename}")

        if write:
            os.system(f"{command} \"{filename}\" \"{output_filename}\"")

    return


# ==========================================================================


def cleanup_filename(filename):
    processed_filename = filename.replace(" Species Spotlight - ", "")
    # processed_filename = processed_filename.replace(" _", "_")
    # processed_filename = processed_filename.replace("_ ", "_")
    return processed_filename.split(".")[0]
    

# ==========================================================================


if __name__ == "__main__":
    main()
