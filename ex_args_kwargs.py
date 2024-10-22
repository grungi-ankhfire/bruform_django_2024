def somme(*args):
    print(args)
    total = 0
    for i in args:
        total += i

    return total

print(somme(1, 5, 4))

def myfunc(*args, **kwargs):
    print(args, kwargs)

myfunc()
myfunc(1)
myfunc(b=1, a=10)
