data = {}

for _ in range(int(input())):
    name, grade = input().split()
    grade = float(grade)
    data[name] = data.get(name, [])
    data[name].append((format(grade, '.2f')))

for key, value in data.items():
    average_grade = sum(float(x) for x in value) / len(value)
    print(f"{key} -> {' '.join(value)} (avg: {average_grade:.2f})")
