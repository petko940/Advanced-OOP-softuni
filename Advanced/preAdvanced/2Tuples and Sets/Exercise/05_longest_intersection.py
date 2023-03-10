max_length = 0
longest_intersection = set()

n = int(input())
for _ in range(n):
    intersection1 = set()
    intersection2 = set()

    range1, range2 = input().split("-")
    first_start, first_end = [int(x) for x in range1.split(",")]
    for x in range(first_start, first_end + 1):
        intersection1.add(x)
    second_start, second_end = [int(x) for x in range2.split(",")]
    for x in range(second_start, second_end + 1):
        intersection2.add(x)

    current_intersection = intersection1.intersection(intersection2)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = intersection1.intersection(intersection2)
        max_length = len(longest_intersection)

output = list(longest_intersection)
print(f"Longest intersection is {output} with length {max_length}")
