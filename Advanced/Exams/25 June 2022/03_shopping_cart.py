""" • Soup: 3
    • Pizza: 4
    • Dessert: 2
"""


def shopping_cart(*args):
    data = {'Soup': [],
            'Pizza': [],
            'Dessert': []}
    for arg in args:
        if arg == "Stop":
            break
        meal, product = arg[0], arg[1]
        data[meal] = data.get(meal, [])

        if meal == "Soup" and len(data[meal]) != 3:
            if product not in data[meal]:
                data[meal].append(product)
        elif meal == "Pizza" and len(data[meal]) != 4:
            if product not in data[meal]:
                data[meal].append(product)
        elif meal == "Dessert" and len(data[meal]) != 2:
            if product not in data[meal]:
                data[meal].append(product)

    if not any(len(x) != 0 for x in data.values()):
        return 'No products in the cart!'

    output = []
    for key, value in sorted(data.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{key}:")
        for v in sorted(value):
            output.append(f" - {v}")

    return '\n'.join(output)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
