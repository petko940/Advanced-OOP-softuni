from collections import deque

programmer_time_to_complete = deque(int(x) for x in input().split())
tasks = deque(int(x) for x in input().split())

rubber_ducky_types = {
    'Darth Vader Ducky': range(0, 61),
    'Thor Ducky': range(61, 121),
    'Big Blue Rubber Ducky': range(121, 181),
    'Small Yellow Rubber Ducky': range(181, 241),
}

result = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while programmer_time_to_complete and tasks:
    first_programmer_time = programmer_time_to_complete.popleft()
    last_task = tasks.pop()

    multiply = first_programmer_time * last_task

    for key, value in rubber_ducky_types.items():
        if multiply in value:
            result[key] += 1
            break
    else:
        programmer_time_to_complete.append(first_programmer_time)
        tasks.append(last_task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f"{key}: {value}") for key, value in result.items()]


# from collections import deque
#
# programmers_time = deque([int(x) for x in input().split()])
# number_of_tasks = [int(x) for x in input().split()]
#
# rubber_ducky_typ = {
#     'Darth Vader Ducky': range(0, 61),
#     'Thor Ducky': range(61, 121),
#     'Big Blue Rubber Ducky': range(121, 181),
#     'Small Yellow Rubber Ducky': range(181, 241),
# }
#
# output = {'Darth Vader Ducky': 0,
#           'Thor Ducky': 0,
#           'Big Blue Rubber Ducky': 0,
#           'Small Yellow Rubber Ducky': 0}
#
# while programmers_time and number_of_tasks:
#     first = programmers_time.popleft()
#     last = number_of_tasks.pop()
#
#     result = first * last
#     for key, value in rubber_ducky_typ.items():
#         if result in value:
#             output[key] = output.get(key, 0) + 1
#             break
#     else:
#         programmers_time.append(first)
#         number_of_tasks.append(last - 2)
#
# print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
#
# for k, v in output.items():
#     print(f"{k}: {v}")
