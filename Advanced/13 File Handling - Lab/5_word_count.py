try:
    file = open('words.txt')
    text_split = file.read().split()
    input_file = open('input.txt')
    input_read = input_file.read().lower().replace("-", "").replace('.', '').replace(',', '').split()
    result = {}
    for word in text_split:
        result[word] = input_read.count(word)
    output = [f"{k} - {v}" for k,v in sorted(result.items(),key=lambda x:-x[1])]

    with open('output.txt','w') as file:
        for x in output:
            file.write(f"{x}\n")

except FileNotFoundError:
    with open('words.txt', "w") as file:
        file.write('quick is fault')

    input_file = ["-I was quick to judge him, but it wasn't his fault.",
                  "-Is this some kind of joke?! Is it?",
                  "-Quick, hide here…It is safer."]
    with open('input.txt', "w") as file:
        for x in input_file:
            file.writelines(f"{x}\n")
    print("Files made. Try again")
