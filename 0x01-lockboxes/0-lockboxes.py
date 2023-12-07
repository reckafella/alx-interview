#!/usr/bin/python3
'''
Module contains a method that determines if all the boxes can be opened
'''


def canUnlockAll(boxes):
    ''' determines if all the boxes can be opened '''
    opened_boxes = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in opened_boxes and\
                    key != box_id:
                opened_boxes.append(key)
    print(opened_boxes)
    return len(opened_boxes) == len(boxes)
