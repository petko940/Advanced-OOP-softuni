odd = set()
even = set()

n = int(input())
for x in range(1, n + 1):
    sum_values = 0
    name = input()
    for char in name:
        sum_values += ord(char)
    sum_values //= x
    if sum_values % 2 == 0:
        even.add(sum_values)
    else:
        odd.add(sum_values)

if sum(odd) == sum(even):
    print(*odd.union(even), sep=", ")
elif sum(odd) > sum(even):
    print(*odd.difference(even), sep=", ")
elif sum(odd) < sum(even):
    print(*odd.symmetric_difference(even), sep=", ")
