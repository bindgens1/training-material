#!/usr/bin/env python

import sys


def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        sys.stderr.write('### error: no input file specified\n')
        return 1
    with open(file_name) as in_file:
        for line in in_file:
            print('|{0}|'.format(line.rstrip('\r\n')))
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
