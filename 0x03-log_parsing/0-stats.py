#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""

import sys


def print_stats(total_size, status_codes):
    """
    Prints the total file size and the count of each status code.
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count:
            print("{}: {}".format(code, count))


def parse_line(line, total_size, status_codes):
    """
    Parses a line of input, updates total_size and status_codes
    """
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[-2]
        if status_code.isdigit():
            total_size += int(parts[-1])
            status_codes[status_code] = status_codes.get(status_code, 0) + 1
    return total_size, status_codes


def main():
    """
    Main function that reads input from stdin, parses each line, and
    prints statistics.
    """
    total_size = 0
    status_codes = {}
    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            total_size, status_codes = parse_line(
                    line, total_size, status_codes)
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
    except BrokenPipeError:

        pass


if __name__ == "__main__":
    main()
