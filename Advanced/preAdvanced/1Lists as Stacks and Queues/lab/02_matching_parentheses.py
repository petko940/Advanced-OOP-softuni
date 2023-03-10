text = input()

lst = []

for index, value in enumerate(text):
    if value == "(":
        lst.append(index)
    elif value == ")":
        start = lst.pop()
        print(text[start:index + 1])
