names = ["Graham", "Kathleen", "Ian", "Cameron", "Cori", "Heather"]

index = 2
print(names[:index])
print(names[index:])

names.append("Beej")
print(names)
names.insert(1, "Serge")
print(names)


numbers = [1, 3, 4, 5, 3, 1, 3, 7, 8]
print(numbers)
while 3 in numbers:
    numbers.remove(3)
print(numbers)


people = ["Corentin","Camille","Joe","Jack"]
filtered = [name for name in people if name[0] != "C"]
print(filtered)

print(people)
person = people.pop(0)
print(people)
print(person)


# Attention à ne pas modifier la liste pendant la boucle sur la même liste
# for i,varnom in enumerate(people) :
#     if varnom[0] == 'C':
#         people.remove(varnom)

# print(people)