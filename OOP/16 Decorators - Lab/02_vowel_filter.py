def vowel_filter(function):
    def wrapper():
        vowels = ["a", "e", "i", "o", "u", "y"]
        letters = function()
        result = [x for x in letters if x in vowels]
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

