#!/usr/bin/python3
"""
Script reads log data from stdin, computes metrics and prints statistics.

Log entries processesed line by line, calculating the total file size and
counting occurrences of different HTTP status codes. Statistics are printed
after every 10 lines, upon keyboard interruption, or at the end of input.
"""

import sys
import re
from collections import defaultdict


def print_stats(total_size, status_codes):
    """
    Print the computed statistics.

    Args:
        total_size (int): The total file size processed.
        status_codes (dict): A dict containing counts of HTTP status codes.

    Returns:
        None
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """
    Parse a log line and extract the status code and file size.

    Args:
        line (str): A single line from the log file.

    Returns:
        tuple: A tuple containing the status code and file size as integers,
               or (None, None) if the line doesn't match the expected format.
    """
    pattern = r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    match = re.match(pattern, line)
    if match:
        return int(match.group(3)), int(match.group(4))
    return None, None


def main():
    """
    Main function to process log data and compute statistics.

    Function reads log data from stdin, computes metrics and prints
    statistics every 10 lines, upon keyboard interruption, or at the
    end of input.

    Returns:
        None
    """
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line.strip())
            if status_code and file_size:
                total_size += file_size
                status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

        # Print final statistics if there's any data processed
        if line_count > 0:
            print_stats(total_size, status_codes)
        else:
            print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
