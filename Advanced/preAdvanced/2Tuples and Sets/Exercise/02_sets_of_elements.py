n, m = [int(x) for x in input().split()]

set1 = set()
set2 = set()

for _ in range(n):
    number = int(input())
    set1.add(number)

for _ in range(m):
    number = int(input())
    set2.add(number)

output = set1.intersection(set2)
# for x in output:
#     print(x)
[print(x) for x in output]
