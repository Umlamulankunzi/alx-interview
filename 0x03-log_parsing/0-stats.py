#!/usr/bin/python3
"""
Log Parsing
"""

import sys
import re

def output(log):
    """
    Helper function to display stats.
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))

if __name__ == "__main__":
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'  # noqa
    )

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
        }
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.match(line)
            if match:
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # Update file size
                log["file_size"] += file_size

                # Update status code frequency
                if code in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                if line_count % 10 == 0:
                    output(log)
    except KeyboardInterrupt:
        pass
    finally:
        output(log)
