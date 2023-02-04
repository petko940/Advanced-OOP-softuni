with open("files/text.txt", "r") as file:
    text = file.readlines()

replaced_symbols = {"-", ",", ".", "!", "?"}
result = []
for line in range(0, len(text), 2):
    for symbol in replaced_symbols:
        text[line] = text[line].replace(symbol, "@")
    result.append(text[line].split()[::-1])

[print(*x) for x in result]
