colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}
"""
Main colors: "red", "yellow", "blue"
Secondary colors: "orange", "purple", "green"
"""

text = input().split()
result = []

while text:
    first = text.pop(0)
    last = text.pop() if len(text) > 0 else ""
    if {first + last}.issubset(colors):
        result.append(first + last)
    elif {last + first}.issubset(colors):
        result.append(last + first)
    else:
        first, last = first[:-1], last[:-1]
        if len(text) % 2 == 0:
            text.insert(len(text) // 2, first) if first else None
            text.insert(len(text) // 2, last) if last else None
        else:
            text.insert(len(text) // 2 + 1, first) if first else None
            text.insert(len(text) // 2 + 1, last) if last else None

for color, combo in secondary_colors.items():
    if color in result:
        if not combo.issubset(result):
            result.remove(color)

print(result)
