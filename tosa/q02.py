def launcher(my_callable, *args, **kwargs):
    return my_callable(*args, **kwargs)


def func1():
    return "Func1 fonctionne!"

def func2(a, b):
    return f"a : {a} et b : {b}"

def func3(a, kw1="first", kw2="second"):
    return f"a : {a}, kw1 : {kw1}, kw2 : {kw2}"

print(launcher(func1))
print(launcher(func2, 15, 30))
print(launcher(func3, 42, kw2="New"))

