from collections import deque


def best_list_pureness(*args):
    list_rotate, number_of_rotations = deque(args[0]), args[1]
    list_len = len(list_rotate)
    result = {
        "0": sum([list_rotate[i] * i for i in range(list_len)])
    }
    for rotation in range(1, number_of_rotations + 1):
        list_rotate.rotate(1)
        result[rotation] = result.get(rotation, sum([list_rotate[i] * i for i in range(list_len)]))
    best_rotation = max(result, key=result.get)

    return f"Best pureness {result[best_rotation]} after {best_rotation} rotations"