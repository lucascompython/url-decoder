#!/usr/bin/env python3
from dataclasses import dataclass
from urllib.parse import unquote
import argparse


@dataclass
class COLORS:
    HEADER: str = '\033[95m'
    OKBLUE: str = '\033[94m'
    OKGREEN: str = '\033[92m'
    WARNING: str = '\033[93m'
    FAIL: str = '\033[91m'
    ENDC: str = '\033[0m'
    BOLD: str = '\033[1m'
    UNDERLINE: str = '\033[4m'

def argumentparser():
    parser = argparse.ArgumentParser(description='URL decoder')
    parser.add_argument('-u', '--url', help='URL to decode')
    args = parser.parse_args()
    return args
    


def main():
    args = argumentparser()
    if not args.url:
        URL = input('Enter URL to decode: ')
    else:
        URL = args.url
    print("\n" + COLORS.OKGREEN + "Decoded URL: " + COLORS.ENDC + unquote(URL) + "\n")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram terminated by user. Exiting...')
        exit(0)
else:
    print('\nPlease execute this file as the main program...')
    exit(0)