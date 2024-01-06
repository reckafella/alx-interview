#!/usr/bin/python3
'''
Module to validate UTF-8
'''


def validUTF8(data):
    ''' validate utf-8 data '''
    try:
        try:
            byte_data = bytes(data)
        except ValueError:
            return False

        decoded_data = byte_data.decode('UTF-8')
        encoded_data = decoded_data.encode('UTF-8')

        return encoded_data == byte_data
    except UnicodeDecodeError:
        return False
