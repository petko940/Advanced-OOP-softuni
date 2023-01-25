numbers = input().split('|')[::-1]

output = []
for x in numbers:
    output.extend(x.split())

print(*output)
