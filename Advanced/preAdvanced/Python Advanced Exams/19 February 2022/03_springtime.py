def start_spring(**kwargs):
    data = {}
    for value, key in kwargs.items():
        data[key] = data.get(key, [])
        data[key].append(value)

    output = []
    for key, value in sorted(data.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{key}:")
        for name in sorted(value):
            output.append(f"-{name}")

    return "\n".join(output)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird", }
print(start_spring(**example_objects))
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
