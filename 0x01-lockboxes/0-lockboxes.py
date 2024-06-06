#!/usr/bin/python3
"""Solve interview puzzle."""


def helper_func(temp_box):
    """Solve interview puzzle."""
    for i, singl in temp_box.items():
        if singl.get('status') == 'opened':
            singl['status'] = 'opened/checked'
            return singl.get('keys')
    return None


def canUnlockAll(boxes):
    """Solve interview puzzle."""
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    temp_hold = {}
    while True:
        if len(temp_hold) == 0:
            temp_hold[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = helper_func(temp_hold)
        if keys:
            for key in keys:
                try:
                    if temp_hold.get(key) and temp_hold.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    temp_hold[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [singl.get('status') for singl in temp_hold.values()]:
            continue
        elif len(temp_hold) == len(boxes):
            break
        else:
            return False

    return len(temp_hold) == len(boxes)
