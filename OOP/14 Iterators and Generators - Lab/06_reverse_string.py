def reverse_text(word):
    for i in word[::-1]:
        yield i


for char in reverse_text("step"):
    print(char, end='')
