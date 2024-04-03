#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    """
    Print the computed statistics including total file size and counts
    of different status codes.

    Args:
        total_size (int): Total size of files processed.
        status_codes (dict): Dictionary containing counts of
        different status codes.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """
    Parses a line of input to extract status code and file size.

    Args:
        line (str): A line of input to parse.

    Returns:
        int, int: Tuple containing status code and file size if
        parsing is successful, else (None, None).
    """
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[-2]
        file_size = parts[-1]
        if status_code.isdigit():
            return int(status_code), int(file_size)
    return None, None


def main():
    """
    Main function to read input, compute statistics, and print them.
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                    405: 0, 500: 0}
    lines_processed = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line.strip())
            if status_code is not None and file_size is not None:
                total_size += file_size
                status_codes[status_code] += 1
                lines_processed += 1

            if lines_processed % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
