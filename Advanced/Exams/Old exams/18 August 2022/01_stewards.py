from collections import deque

seats = input().split(', ')

first_numbers = deque([int(x) for x in input().split(', ')])
second_numbers = deque([int(x) for x in input().split(', ')])

seat_matches, rotations = 0, 0
matches = []

while len(matches) != 3 and rotations != 10 and first_numbers and second_numbers:
    first = first_numbers.popleft()
    last = second_numbers.pop()
    sum = first + last
    char = chr(sum)
    for i in seats:
        if char in i and i not in matches:
            if first == int(i[:-1]):
                matches.append(i)
                seats.remove(i)
                break
            if last == int(i[:-1]):
                matches.append(i)
                seats.remove(i)
                break
    else:
        first_numbers.append(first)
        second_numbers.appendleft(last)
    rotations += 1

print(f"Seat matches: {', '.join([x for x in matches])}")
print(f"Rotations count: {rotations}")
