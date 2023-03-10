numbers1 = [int(x) for x in input().split()]
numbers2 = [int(x) for x in input().split()]
numbers1 = set(numbers1)
numbers2 = set(numbers2)

n = int(input())
for _ in range(n):
    active1, active2, *numbers = [int(x) if x.isdigit() else x for x in input().split()]
    active = active1 + " " + active2
    if "Add First" in active:
        numbers1.update(numbers)
    elif "Add Second" in active:
        numbers2.update(numbers)
    elif "Remove First" in active:
        numbers1.difference_update(numbers)
    elif "Remove Second" in active:
        numbers2.difference_update(numbers)
    elif "Check Subset" in active:
        print(numbers2.issubset(numbers1))

output1 = list(sorted(numbers1))
print(*output1, sep=", ")

output2 = list(sorted(numbers2))
print(*output2, sep=", ")
