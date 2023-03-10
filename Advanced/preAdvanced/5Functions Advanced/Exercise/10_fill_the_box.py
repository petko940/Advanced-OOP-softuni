def fill_the_box(*args):
    index = 0
    for x in range(len(args)):
        if args[x] != "Finish":
            index += 1
        if args[x] == "Finish":
            break
    box_size = args[0] * args[1] * args[2]
    number_boxes = 0
    for x in range(3, index):
        number_boxes += args[x]
    if box_size >= number_boxes:
        return f"There is free space in the box. You could put {box_size - number_boxes} more cubes."
    else:
        return f"No more free space! You have {abs(box_size - number_boxes)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
