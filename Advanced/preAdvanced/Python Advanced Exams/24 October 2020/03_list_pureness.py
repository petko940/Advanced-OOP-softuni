from collections import deque


def best_list_pureness(*args):
    list_rotate = deque(args[0])
    rotate_count = args[1]
    list_len = len(list_rotate)
    result = {"0": sum([list_rotate[i] * i for i in range(list_len)])}
    for rotation in range(1, rotate_count + 1):
        list_rotate.rotate(1)
        result[rotation] = result.get(rotation, sum([list_rotate[i] * i for i in range(list_len)]))
    best_rotation = max(result, key=result.get)
    return f"Best pureness {result[best_rotation]} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
