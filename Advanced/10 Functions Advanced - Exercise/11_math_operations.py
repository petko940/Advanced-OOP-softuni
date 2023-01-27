def math_operations(*args, **kwargs):
    added = [args[i] for i in range(len(args)) if i % 4 == 0]
    subtracted = [args[i] for i in range(len(args)) if i % 4 == 1]
    divisor = [args[i] for i in range(len(args)) if i % 4 == 2]
    multiplied = [args[i] for i in range(len(args)) if i % 4 == 3]
    for a in added:
        kwargs['a'] += a
    for s in subtracted:
        kwargs['s'] -= s
    for d in divisor:
        if d != 0:
            kwargs['d'] /= d
    for m in multiplied:
        kwargs['m'] *= m
    output = [f"{k}: {v:.1f}" for k, v in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]
    return '\n'.join(output)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
