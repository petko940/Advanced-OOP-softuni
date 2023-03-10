from collections import deque

seats = input().split(", ")
numbers_one = deque([int(x) for x in input().split(", ")])
numbers_two = deque([int(x) for x in input().split(", ")])

rotations = 0
taken_seats = []
while len(taken_seats) != 3 and rotations != 10:
    one = numbers_one.popleft()
    two = numbers_two.pop()
    ascii_sum = chr(one + two)
    rotations += 1
    for x in seats:
        if ascii_sum in x:
            if one == int(x[:-1]):
                taken_seats.append(x)
                seats.remove(x)
                break
            if two == int((x[:-1])):
                taken_seats.append(x)
                seats.remove(x)
                break
    else:
        numbers_one.append(one)
        numbers_two.appendleft(two)

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
