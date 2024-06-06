#!/usr/bin/python3
"""Solve interview puzzle."""


def helper_func(temp_box):
    """Solve interview puzzle."""
    for x, singl in temp_box.items():
        if singl.get('status') == 'opened':
            singl['status'] = 'opened/checked'
            return singl.get('keys')
    return None


def canUnlockAll(boxes):
    """Solve interview puzzle."""
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    temp_box = {}
    while True:
        if len(temp_box) == 0:
            temp_box[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = helper_func(temp_box)
        if keys:
            for key in keys:
                try:
                    if temp_box.get(key) and temp_box.get(key) \
                        .get('status') == 'opened/checked':
                        continue
                    temp_box[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [singl.get('status') for singl in temp_box.values()]:
            continue
        elif len(temp_box) == len(boxes):
            break
        else:
            return False

    return len(temp_box) == len(boxes)
