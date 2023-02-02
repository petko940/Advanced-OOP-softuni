def start_spring(**kwargs):
    global value
    data = {}
    for name, type in kwargs.items():
        data[type] = data.get(type, [])
        data[type].append(name)

    result = []
    for key, value in sorted(data.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{key}:")
        for v in sorted(value):
            result.append(f"-{v}")

    return '\n'.join(result)


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
