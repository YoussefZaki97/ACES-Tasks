from random import randint

comp = [randint(1, 9), randint(1, 9), randint(1, 9)]

for x in range(0, 9):
    if comp[1] == comp[0]:
        comp[1] = randint(1, 9)
    else:
        break

for y in range(0, 9):
    if comp[2] == comp[0] or comp[2] == comp[1]:
        comp[2] = randint(1, 9)
    else:
        break

print(comp)

status = 0
w = [0, 0, 0]
while status == 0:

    x1 = int(input("Enter a number from Zero to Nine: \n"))
    x2 = int(input("Enter your second number: \n"))
    x3 = int(input("Enter your third number: \n"))

    match = 0
    close = 0
    none = 0

    user = [x1, x2, x3]


    for i in range(0, 3):

        if user[i] == comp[i]:
            w[i] = 1
            match = 1
            break


        elif user[i] != comp[i]:
            for ii in range(0, 3):
                if user[i] == comp[ii]:
                    close = 1
                    break
            if match == 0 and close == 0:
                none = 1
                break








    if w[0] == 1 and w[1] == 1 and w[2] == 1:
        status = 1
        print(" YOU WIN!")
        break

    if match == 1:
        print("Match")

    if close == 1:
        print("Close")

    if none == 1:
        print("None")






