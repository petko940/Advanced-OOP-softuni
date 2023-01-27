def fill_the_box(height, length, width, *cubes):
    box_size = height * length * width
    current_size = box_size
    continue_fill = True
    cubes_left = 0
    for cube in cubes:
        if cube == "Finish":
            break
        if continue_fill:
            if current_size >= cube:
                current_size -= cube
            else:
                cube -= current_size
                continue_fill = False
                cubes_left += cube
        else:
            cubes_left += cube

    if cubes_left == 0:
        return f"There is free space in the box. You could put {current_size} more cubes."

    return f"No more free space! You have {cubes_left} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
