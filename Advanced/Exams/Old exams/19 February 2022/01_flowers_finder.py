from collections import deque

vowels = deque([x for x in input().split()])
consonants = deque([x for x in input().split()])

""" • "rose"
    • "tulip"
    • "lotus"
    • "daffodil
"""

flowers = ["rose", "tulip", "lotus", "daffodil"]
word_found = ''
is_found = False
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    temporary_word = word_found
    for flower in flowers:
        if vowel in flower:
            word_found += vowel
        if consonant in flower:
            word_found += consonant
        for char in flower:
            if char in word_found:
                is_found = True
            else:
                is_found = False
                break
        if is_found:
            print(f"Word found: {flower}")
            break
    if is_found:
        break
else:
    print('Cannot find any word!')

if vowels:
    print(f"Vowels left: {' '.join([str(x) for x in vowels])}")

if consonants:
    print(f"Consonants left: {' '.join([str(x) for x in consonants])}")


