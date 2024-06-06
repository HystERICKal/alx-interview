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

    aux = {}
    while True:
        if len(aux) == 0:
            aux[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = helper_func(aux)
        if keys:
            for key in keys:
                try:
                    if aux.get(key) and aux.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    aux[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [singl.get('status') for singl in aux.values()]:
            continue
        elif len(aux) == len(boxes):
            break
        else:
            return False

    return len(aux) == len(boxes)
