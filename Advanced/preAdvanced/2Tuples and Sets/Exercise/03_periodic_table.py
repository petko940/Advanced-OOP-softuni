elements = set()

number_lines = int(input())

for _ in range(number_lines):
    element = input().split()
    for ele in element:
        elements.add(ele)

print("\n".join(elements))
