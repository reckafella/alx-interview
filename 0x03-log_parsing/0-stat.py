#!/usr/bin/python3

import re
import sys


def create_log_dict() -> dict:
    status_codes: list = [200, 301, 400, 401, 403, 404, 405, 500]

    log_dict: dict = {
        'file_size': 0,
        'status_codes': {str(code): 0 for code in status_codes}
    }

    return log_dict


def parse_single_line(line, regx, log_dict: dict) -> dict:
    '''
    parses a single line to increment file_size and status_codes
    '''
    match = regx.fullmatch(line)

    if match:
        status_code, file_size = match.group(1, 2)
        
        new_log_dict = log_dict.copy()  # Create a new dictionary
        new_log_dict['file_size'] += int(file_size)
        
        if status_code.isdecimal():
            new_log_dict['status_codes'][status_code] += 1

        return new_log_dict

    return log_dict


def print_result(log_dict: dict):
    print('File size: {}'.format(log_dict['file_size']))

    sorted_codes: list = sorted(log_dict['status_codes'])

    for status_code in sorted_codes:
        if log_dict['status_codes'][status_code]:
            print(f"{status_code}: {log_dict['status_codes'][status_code]}")


def execute():
    regx = re.compile(r'\d{1, 3}\.\d{1, 3}\.\d{1, 3}\.\d{1, 3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')

    log_dict: dict = create_log_dict()
    
    line_count: int = 0

    for line in sys.stdin:
        line = line.strip()
        
        line_count = line_count + 1

        log_dict = parse_single_line(line, regx, log_dict)

        try:
            if line_count % 10 == 0:
                print_result(log_dict)
        except KeyboardInterrupt:
            print_result(log_dict)


if __name__ == '__main__':
    execute()
