def words_sorting(*args):
    dictionary = {}
    for arg in args:
        sum_ascii = 0
        for char in arg:
            sum_ascii += ord(char)
        dictionary[arg] = sum_ascii

    output = []
    if sum(dictionary.values()) % 2 != 0:
        for key, value in sorted(dictionary.items(), key=lambda item: -item[1]):
            output.append(f"{key} - {value}")
    else:
        for key, value in sorted(dictionary.items(), key=lambda item: item[0]):
            output.append(f"{key} - {value}")

    return "\n".join(output)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
