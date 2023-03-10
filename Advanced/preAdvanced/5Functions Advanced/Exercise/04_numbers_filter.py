def even_odd_filter(**kwargs):
    new_list = {}
    for key, value in kwargs.items():
        for v in value:
            new_list[key] = new_list.get(key, [])
            if key == "odd":
                if v % 2 != 0:
                    new_list[key].append(v)
            else:
                if v % 2 == 0:
                    new_list[key].append(v)
    output = {}
    for key, value in sorted(new_list.items()):
        output[key] = output.get(key, value)
    return new_list


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
