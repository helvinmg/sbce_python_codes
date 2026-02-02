def smallsq(*args):
    small=args[0]
    for num in args:
        if num<small:
            small=num
    return small**2

