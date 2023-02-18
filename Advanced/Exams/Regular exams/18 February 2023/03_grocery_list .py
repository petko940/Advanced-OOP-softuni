def shop_from_grocery_list(budget, grocery_list, *args):
    data = grocery_list
    for arg in args:
        if arg[0] in data:
            if budget >= arg[1]:
                budget -= arg[1]
                data.remove(arg[0])
            else:
                break

    if not data:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join([x for x in grocery_list])}."
