def palindrome(*args):
    if args[0] == args[0][::-1]:
        return f"{args[0]} is a palindrome"
    return f"{args[0]} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
