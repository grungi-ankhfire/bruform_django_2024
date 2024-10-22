
# Infinite loop
# while True:
#     print("Oops...")

a = 0
while a < 100:
    print(a)
    a += 1
    break

a = 0
while a < 20:
    print(a)
    a += 1
    if a % 5:
        continue
    print("---")

# a = 0
# while a < 20:
#     if a % 5 == 0:
#         print(a)
#         print("---") 
#     else:
#         print(a)
#     a += 1
