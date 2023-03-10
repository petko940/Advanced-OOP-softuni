def shopping_list(budget, **kwargs):
    if budget >= 100:
        output = []
        basket = 0
        for product, value in kwargs.items():
            if basket == 5 or budget <= 0:
                break
            price, quantity = value[0], value[1]
            if price * quantity <= budget:
                basket += 1
                budget -= price * quantity
                output.append(f"You bought {product} for {price * quantity:.2f} leva.")
        return "\n".join(output)

    return "You do not have enough budget."


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
