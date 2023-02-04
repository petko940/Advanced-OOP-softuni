from string import ascii_letters, punctuation

with open("files/text.txt", "r") as file:
    text = file.readlines()

output = []
for i in range(len(text)):
    letters, punctuations = 0, 0
    for char in text[i]:
        if char in ascii_letters:
            letters += 1
        elif char in punctuation:
            punctuations += 1

    output.append(f"Line {i + 1}: {text[i][:-1]} ({letters})({punctuations})")

with open('files/output.txt','w') as file:
    for x in output:
        file.write(f'{x}\n')

