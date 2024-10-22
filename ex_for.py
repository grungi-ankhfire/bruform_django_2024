for i in range(10):
    print("Coucou")

names = ["Graham", "Kathleen", "Cameron", "Cori", "Ian", "Heather"]
for person in names:
    if len(person) > 7:
        continue
    print(person + " is here!")
    if person == "Ian":
        break
