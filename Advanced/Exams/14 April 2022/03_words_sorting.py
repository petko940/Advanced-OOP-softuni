def words_sorting(*args):
    result = {}
    for word in args:
        value = 0
        for char in word:
            value += ord(char)
        result[word] = value

    even_ord_odd = sum(result.values())
    output = []
    if even_ord_odd % 2 == 0:
        for key, value in sorted(result.items(), key=lambda x: x[0]):
            output.append(f"{key} - {value}")
    else:
        for key, value in sorted(result.items(), key=lambda x: -x[1]):
            output.append(f"{key} - {value}")
    return "\n".join(output)
