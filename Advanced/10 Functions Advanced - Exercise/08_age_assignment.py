def age_assignment(*names, **ages):
    result = {}
    for name in names:
        for key, value in ages.items():
            if name.startswith(key):
                result[name] = value
                break
    output = [f"{n} is {a} years old." for n, a in sorted(result.items(), key=lambda x: x[0])]
    return '\n'.join(output)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
