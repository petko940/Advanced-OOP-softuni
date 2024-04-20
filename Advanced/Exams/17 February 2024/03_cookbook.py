def cookbook(*args):
    result = {}

    for arg in args:
        recipe_name, cuisine, list_of_ingredients = arg
        if cuisine not in result:
            result[cuisine] = {}

        result[cuisine][recipe_name] = list_of_ingredients

    output = []
    for key, value in sorted(result.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{key} cuisine contains {len(value)} recipes:")
        for name, ing in sorted(value.items()):
            output.append(f"  * {name} -> Ingredients: {', '.join(ing)}")

    return '\n'.join(output)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
))
