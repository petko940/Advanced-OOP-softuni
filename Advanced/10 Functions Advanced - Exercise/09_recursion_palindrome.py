def palindrome(word, index):
    first, last = 0, -1
    for i in range(len(word) // 2):
        if word[first] != word[last]:
            return f"{word} is not a palindrome"
        first += 1
        last -= 1
    else:
        return f"{word} is a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
