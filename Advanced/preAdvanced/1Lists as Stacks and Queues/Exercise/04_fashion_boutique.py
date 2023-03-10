box_of_clothes = [int(x) for x in input().split()]
capacity = int(input())
cap = capacity
count = 1
while box_of_clothes:
    current_box = box_of_clothes.pop()
    if current_box > cap:
        box_of_clothes.append(current_box)
        count += 1
        cap = capacity
    else:
        cap -= current_box

print(count)
