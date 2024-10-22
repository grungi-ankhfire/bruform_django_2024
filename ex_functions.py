from random import randint

def say_hello():
    print("Hello there!")

say_hello()
say_hello()

def dice(dice_number = 1, faces = 6):
    total = 0

    for n in range(dice_number):
        result = randint(1, faces)
        total += result

    return total

print(dice(faces=20))
