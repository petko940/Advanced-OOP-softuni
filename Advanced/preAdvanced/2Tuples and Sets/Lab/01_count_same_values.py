numbers = [float(x) for x in input().split()]

data = {}
for n in numbers:
    data[n] = data.get(n, 0)
    data[n] += 1

for number, count in data.items():
    print(f"{number} - {count} times")
