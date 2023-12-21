#!/usr/bin/python3
'''
log parsing module code
'''
import re
import sys


def create_log_dict() -> dict:
    '''
    create an initial dict of file size and status codes
    '''
    status_codes: list = [200, 301, 400, 401, 403, 404, 405, 500]

    log_dict: dict = {
        'file_size': 0,
        'status_codes': {str(code): 0 for code in status_codes}
    }

    return log_dict


def parse_line(line: str, regx: re.Pattern[str], log_dict: dict) -> dict:
    '''
    parses a single line to increment file_size and status_codes
    '''
    match = regx.fullmatch(line)

    if match:
        status_code, file_size = match.group(1, 2)

        log_dict['file_size'] += int(file_size)

        if status_code.isdecimal():
            log_dict['status_codes'][status_code] += 1

    return log_dict


def print_result(log_dict: dict) -> None:
    '''
    handles the printing of file_size and status_codes
    '''
    print('File size: {}'.format(log_dict['file_size']))

    sorted_codes: list = sorted(log_dict['status_codes'])

    for status_code in sorted_codes:
        if log_dict['status_codes'][status_code]:
            print(f"{status_code}: {log_dict['status_codes'][status_code]}")


def execute():
    '''
    execute the program
    '''
    regx = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')

    log_dict: dict = create_log_dict()

    line_count: int = 0

    for line in sys.stdin:
        line = line.strip()

        line_count = line_count + 1

        parsed_dict: dict = parse_line(line, regx, log_dict)

        try:
            if line_count % 10 == 0:
                print_result(parsed_dict)
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    execute()
