#!/usr/bin/python3
"""
module for log parsing
"""

import sys


def parse_log_line(line):
    """
    Parses a log line and extracts status code and file size.
    Returns a tuple (status_code, file_size).
    """
    try:
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except (IndexError, ValueError):
        return None, None


def print_statistics(total_file_size, status_code_counts):
    """
    Prints total file size and number of lines by status code.
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if code in [200, 301, 400, 401, 403, 404, 405, 500]:
            print("{}: {}".format(code, status_code_counts[code]))


def main():
    """
    main func
    """

    total_file_size = 0
    status_code_counts = {}

    try:
        line_num = 0
        for line in sys.stdin:
            line = line.strip()
            status_code, file_size = parse_log_line(line)
            if status_code is not None:
                total_file_size += file_size
                status_code_counts[status_code] = status_code_counts.get(
                        status_code, 0) + 1

            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_code_counts)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)
        raise


if __name__ == "__main__":
    main()
