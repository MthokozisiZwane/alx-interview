#!/usr/bin/python3

from collections import deque


def canUnlockAll(boxes):
    n = len(boxes)
    visited_boxes = [False] * n
    visited_boxes[0] = True

    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited_boxes[key]:
                visited_boxes[key] = True
                queue.append(key)
    return all(visited_boxes)
