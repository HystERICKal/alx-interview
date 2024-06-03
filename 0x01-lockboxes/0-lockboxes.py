#!/usr/bin/python3

def helper_func(tempy):
    for i, j in tempy.items():
        if j.get('status') == 'opened':
            j['status'] = 'opened/checked'
            return j.get('keys')
    return None


def canUnlockAll(boxes):
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    tempp = {}
    while True:
        if len(tempp) == 0:
            tempp[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = helper_func(tempp)
        if keys:
            for key in keys:
                try:
                    if tempp.get(key) and tempp.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    tempp[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, iError):
                    continue
        elif 'opened' in [j.get('status') for j in tempp.values()]:
            continue
        elif len(tempp) == len(boxes):
            break
        else:
            return False

    return len(tempp) == len(boxes)
