data = {}

numbers = [float(x) for x in input().split()]
for x in numbers:
    data[x] = data.get(x, 0) + 1

[print(f"{k} - {v} times") for k, v in data.items()]
