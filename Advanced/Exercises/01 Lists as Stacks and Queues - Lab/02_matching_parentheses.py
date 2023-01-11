data = list(input())
indexes = []

for i in range(len(data)):
    check = data[i]
    if check == "(":
        indexes.append(i)
    elif check == ")":
        index = indexes.pop()
        print(*data[index:i + 1], sep="")
