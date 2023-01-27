def even_odd_filter(**kwargs):
    if 'even' in kwargs.keys():
        kwargs['even'] = [x for x in kwargs['even'] if x % 2 == 0]
    if 'odd' in kwargs.keys():
        kwargs['odd'] = [x for x in kwargs['odd'] if x % 2 != 0]

    result = sorted(kwargs.items(), key=lambda x: -len(x[1]))
    return dict(result)


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
