#!/usr/bin/python3
'''
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can
be opened.
'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened'''
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    stack = [0]
    visited[0] = True

    while stack:
        current_box = stack.pop()

        # Iterate through keys in the current box
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
