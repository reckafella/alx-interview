#!/usr/bin/python3
'''
Module contains a method that determines if all the boxes can be opened
'''


def canUnlockAll(boxes):
    ''' determines if all the boxes can be opened '''
    for key in range(1, len(boxes)):
        unlocked = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                unlocked = True
                break
        if not unlocked:
            return False
    return True
