def shopping_cart(*args):
    data = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }
    for arg in args:
        if arg == "Stop":
            break
        type_meal, product = arg[0], arg[1]

        if type_meal == "Soup" and len(data[type_meal]) != 3:
            if product not in data[type_meal]:
                data[type_meal].append(product)
        elif type_meal == "Pizza" and len(data[type_meal]) != 4:
            if product not in data[type_meal]:
                data[type_meal].append(product)
        elif type_meal == "Dessert" and len(data[type_meal]) != 2:
            if product not in data[type_meal]:
                data[type_meal].append(product)

    if not any(len(x) != 0 for x in data.values()):
        return "No products in the cart!"
    output = []
    for key, value in sorted(data.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{key}:")
        for v in sorted(value):
            output.append(f" - {v}")
    return "\n".join(output)


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

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

