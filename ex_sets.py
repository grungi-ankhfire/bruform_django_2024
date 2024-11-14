numbers = {1, 3, 4}
print(numbers)
numbers.add(2)
numbers.add(1)
print(numbers)
for x in numbers:
    print(x)

print(4 in numbers)

print(type({}))  # {} est un dictionnaire, pas un set
set()  # Crée un set vide

print("-----")

mylist = ["a", "c", "a", "p", "b", "d", "a", "c", "e", "f", "a"]
myset = set(mylist)
print(myset)
print(len(myset))

myset2 = set()
for i in mylist:
    myset2.add(i)
print(myset2)

myset3 = {x for x in mylist}
print(myset3)