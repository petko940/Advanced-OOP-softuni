from collections import deque


def list_manipulator(*args):
    numbers = deque(args[0])
    if args[1] == "add":
        if args[2] == "beginning":
            for x in range(len(args) - 1, len(args[3:]) - 1, -1):
                numbers.appendleft(args[x])
        elif args[2] == "end":
            for x in range(len(args[3:]), len(args)):
                numbers.append(args[x])
    elif args[1] == 'remove':
        if args[2] == "beginning":
            if len(args) > 3:
                for _ in range(args[3]):
                    numbers.popleft()
            else:
                numbers.popleft()
        elif args[2] == "end":
            if len(args) > 3:
                for _ in range(args[3]):
                    numbers.pop()
            else:
                numbers.pop()

    return [x for x in numbers]


# print(list_manipulator([1,2,3], "remove", "end"))
# print(list_manipulator([1,2,3], "remove", "beginning"))
# print(list_manipulator([1,2,3], "add", "beginning", 20))
# print(list_manipulator([1,2,3], "add", "end", 30))
# print(list_manipulator([1,2,3], "remove", "end", 2))
# print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
