from collections import deque

amount_of_money = deque([int(x) for x in input().split()])
prices_of_food = deque([int(x) for x in input().split()])
food_count = 0

while amount_of_money and prices_of_food:
    money_last = amount_of_money.pop()
    price_first = prices_of_food.popleft()

    if money_last == price_first:
        food_count += 1
    elif money_last > price_first:
        money_last -= price_first
        if amount_of_money:
            amount_of_money[-1] += money_last
        else:
            amount_of_money.append(money_last)
        food_count += 1

if not food_count:
    print(f"Henry remained hungry. He will try next weekend again.")
else:
    if food_count >= 4:
        print(f"Gluttony of the day! Henry ate {food_count} foods.")
    else:
        print(f"Henry ate: {food_count} food{'' if food_count == 1 else 's'}.")
