n = 3
if n == 1:
    pass
elif n == 2:
    pass
elif n == 3:
    pass

match n:
    case 1:
        pass
    case 2:
        pass
    case 3:
        pass
    case _:
        pass

numbers = (5, 12)
match numbers:
    case (1, 2):
        pass
    case (5, y):
        print(y)