from collections import deque

expressions = input().split()
numbers = deque()
start = expressions[0]
result = int(start)

for expression in expressions[1:]:
    if expression not in "+-/*":
        numbers.append(int(expression))
    else:
        if expression == "+":
            while numbers:
                result += numbers.popleft()
        elif expression == "-":
            while numbers:
                result -= numbers.popleft()
        elif expression == "*":
            while numbers:
                result *= numbers.popleft()
        elif expression == "/":
            while numbers:
                result //= numbers.popleft()

print(abs(result))
