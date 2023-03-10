def age_assignment(*args, **kwargs):
    names = [x for x in args]
    data = {}
    for name, age in kwargs.items():
        for n in names:
            if name == n[0]:
                data[n] = age
    output = ""
    for key, value in sorted(data.items(), key=lambda x: x[0]):
        output += f"{key} is {value} years old.\n"

    return output


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
