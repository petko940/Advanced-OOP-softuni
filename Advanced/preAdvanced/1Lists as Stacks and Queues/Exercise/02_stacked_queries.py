stack = []

n = int(input())
for _ in range(n):
    query = input().split()
    if query[0] == '1':
        stack.append(int(query[1]))
    if stack:
        if query[0] == '2':
            stack.pop()
        elif query[0] == '3':
            print(max(stack))
        elif query[0] == '4':
            print(min(stack))

output = [str(x) for x in stack[::-1]]
print(', '.join(output))
