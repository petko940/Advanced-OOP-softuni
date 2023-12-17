def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    basket = 5
    data = {}
    for product, price in kwargs.items():
        whole_price = price[0] * price[1]
        if whole_price <= budget:
            data[product] = whole_price
            basket -= 1
            budget -= whole_price
            if basket == 0 or budget <= 0:
                break
    output = [f"You bought {k} for {v:.2f} leva." for k, v in data.items()]
    return '\n'.join(output)


print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
