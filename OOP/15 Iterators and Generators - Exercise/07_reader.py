def read_next(*args):
    for x in args:
        for y in x:
            yield y
