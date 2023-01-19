one = set([int(x) for x in input().split()])
two = set([int(x) for x in input().split()])

commands = {
    "Add First": lambda x: [one.add(element) for element in x],
    "Add Second": lambda x: [two.add(element) for element in x],
    "Remove First": lambda x: [one.discard(element) for element in x],
    "Remove Second": lambda x: [two.discard(element) for element in x],
    "Check Subset": lambda: print(True) if two.issubset(one) else print(False)
}

for _ in range(int(input())):
    command_one, command_two, *data = \
        [int(x) if x.isdigit() else x for x in input().split()]
    event = command_one + " " + command_two
    if data:
        commands[event](int(x) for x in data)
    else:
        commands[event]()

print(*sorted(one), sep=", ")
print(*sorted(two), sep=", ")
