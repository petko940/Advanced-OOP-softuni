number_of_students = int(input())

data = {}
for _ in range(number_of_students):
    name, grade = input().split()
    grade = float(grade)
    data[name] = data.get(name, [])
    data[name].append(format(grade, '.2f'))

for student, grades in data.items():
    average = sum([float(x) for x in grades]) / len(grades)
    print(f"{student} -> {' '.join(grades)} (avg: {average:.2f})")
