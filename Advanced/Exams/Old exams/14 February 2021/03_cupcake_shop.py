def stock_availability(*args):
    boxes = args[0]
    if args[1] == 'delivery':
        for x in args[2:]:
            boxes.append(x)
    elif args[1] == 'sell':
        if str(args[-1]).isdigit():
            for _ in range(args[-1]):
                boxes.pop(0)
        elif args[-1] == 'sell':
            boxes.pop(0)
        else:
            for x in range(2, len(args)):
                c = boxes.count(args[x])
                for _ in range(c):
                    boxes.remove(args[x])

    output = [f"{x}" for x in boxes]
    return output


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
