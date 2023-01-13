stack = []

query_types = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}

for _ in range(int(input())):
    query = [int(x) for x in input().split()]
    query_types[query[0]](query)

stack.reverse()
print(*stack, sep=", ")
