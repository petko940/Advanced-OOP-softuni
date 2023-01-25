def sorting_cheeses(**kwargs):
    output = []
    for cheese, quantity in sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(cheese)
        for v in sorted(quantity, reverse=True):
            output.append(v)
    return '\n'.join([str(x) for x in output])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
