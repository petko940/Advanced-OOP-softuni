"""
    • "rose"
    • "tulip"
    • "lotus"
    • "daffodil"
"""

from collections import deque

vowels = deque([x for x in input().split()])
consonants = deque([x for x in input().split()])

flowers = ["rose", "tulip", "lotus", "daffodil"]
items = ["rose", "tulip", "lotus", "daffodil"]
output = ""
is_ready = False
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    if vowel or consonant in flowers[0]:
        flowers[0] = flowers[0].replace(vowel, "").replace(consonant, "")
        if not flowers[0]:
            output = items[0]
            is_ready = True
    if vowel or consonant in flowers[1]:
        flowers[1] = flowers[1].replace(vowel, "").replace(consonant, "")
        if not flowers[1]:
            output = items[1]
            is_ready = True
    if vowel or consonant in flowers[2]:
        flowers[2] = flowers[2].replace(vowel, "").replace(consonant, "")
        if not flowers[2]:
            output = items[2]
            is_ready = True
    if vowel or consonant in flowers[3]:
        flowers[3] = flowers[3].replace(vowel, "").replace(consonant, "")
        if not flowers[3]:
            output = items[3]
            is_ready = True
    if is_ready:
        print(f"Word found: {output}")
        break
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
