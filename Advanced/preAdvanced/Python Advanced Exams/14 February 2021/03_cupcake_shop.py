def stock_availability(*args):
    inventory = args[0]  # list
    if args[1] == "delivery":
        for arg in args[2:]:
            inventory.append(arg)
    else:
        if str(args[-1]).isdigit():
            for _ in range(args[-1]):
                inventory.pop(0)
        elif args[-1] == "sell":
            inventory.pop(0)
        else:
            for x in range(2, len(args)):
                if args[x] in inventory:
                    check = args[x]
                    inventory = list(filter(lambda x: x != check, inventory))

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
