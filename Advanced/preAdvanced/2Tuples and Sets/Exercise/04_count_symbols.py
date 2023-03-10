output = {}

text = input()
for char in text:
    output[char] = output.get(char, 0) + 1

for key, value in sorted(output.items(), key=lambda x: x[0]):
    print(f"{key}: {value} time/s")
