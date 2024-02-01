#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 12, 25], 1137))

print(makeChange([125, 54, 48, 11, 105], 25144558))
