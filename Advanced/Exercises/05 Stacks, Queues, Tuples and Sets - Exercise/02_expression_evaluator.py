from collections import deque

expression = deque(input().split())
temp = []

while not expression[-1].isdigit():
    current_element = expression.popleft()

    if current_element.lstrip("-").isdigit():
        temp.append(int(current_element))
    else:
        if current_element == "*":
            while len(temp) > 1:
                temp.insert(0, (temp.pop(0) * temp.pop(0)))
        elif current_element == "-":
            while len(temp) > 1:
                temp.insert(0, (temp.pop(0) - temp.pop(0)))
        elif current_element == "+":
            while len(temp) > 1:
                temp.insert(0, (temp.pop(0) + temp.pop(0)))
        elif current_element == "/":
            while len(temp) > 1:
                temp.insert(0, (temp.pop(0) // temp.pop(0)))
        expression.appendleft(str(temp[0]))
        temp.clear()

print(*expression)
