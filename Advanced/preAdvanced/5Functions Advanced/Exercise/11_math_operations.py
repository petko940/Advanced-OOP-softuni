def math_operations(*args, **kwargs):
    added = [args[x] for x in range(len(args)) if x % 4 == 0]
    subtracted = [args[x] for x in range(len(args)) if x % 4 == 1]
    divisor = [args[x] for x in range(len(args)) if x % 4 == 2]
    multiplier = [args[x] for x in range(len(args)) if x % 4 == 3]
    data = {}
    for key, value in kwargs.items():
        if key == "a":
            added = sum(added) + value
            data[key] = added
        elif key == "s":
            subtracted = sum(subtracted) - value
            print(f"{subtracted:.1f}")
            data[key] = subtracted
        elif key == "d":
            if value != 0:
                divisor = sum(divisor) / value
            else:
                divisor = 0
            data[key] = divisor
        elif key == "m":
            multiplier = sum(multiplier) * value
            data[key] = multiplier
    output = ""
    for key, value in sorted(data.items(), key=lambda x: (-x[1], x[0])):
        output += f"{key}: {value:.1f}\n"
    return output


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
