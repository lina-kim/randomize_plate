#!/usr/bin/python3

from pathlib import Path
import argparse
import pandas as pd


def arg_parse():
    parser = argparse.ArgumentParser()

    # Required user-input arguments
    parser.add_argument(
        "-i",
        "--input_dir",
        help="Path to directory containing FASTQ files.",
        type=str,
        required=True,
    )

    args = parser.parse_args()
    return args


def main(args):
    pass


if __name__ == "__main__":
    cli_args = arg_parse()
    main(cli_args)
