

import random

computer = random.choice([-1, 0, 1])
youstr = input("enter a number :")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reversDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

print(f"you chose {reversDict[you]}\ncomputer chose {reversDict[computer]}")


if(computer == you):
    print("its draw")

else:
    if(computer == -1 and you == 1):
        print("its win")
    elif(computer == -1 and you == 0):
        print("it lose")
    elif(computer == 1 and you == -1):
        print("its lose")
    elif(computer == 1 and you == 0):
        print("its win")
    elif(computer == 0 and you == 1):
        print("its lose")
    elif(computer == 0 and you == -1):
        print("it lose")
    else:
        print("something get worng")