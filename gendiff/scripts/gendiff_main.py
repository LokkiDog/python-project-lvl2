#!/usr/bin/env python
from gendiff.generate_diff import generate_diff
import argparse

def main():
    """Some documentation about gendiff"""

    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
