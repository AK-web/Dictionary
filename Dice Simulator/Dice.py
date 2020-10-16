import random

print("This is the dice simulator")
y="z"
while y == "z":
    X = random.randint(1,6)

    if X == 1:
        print("-------")
        print("|     |")
        print("|  o  |")
        print("|     |")
        print("-------")
    elif X == 2:
        print("-------")
        print("|     |")
        print("| o o |")
        print("|     |")
        print("-------")
    elif X == 3:
        print("-------")
        print("|     |")
        print("|o o o|")
        print("|     |")
        print("-------")
    elif X == 4:
        print("-------")
        print("| o o |")
        print("|     |")
        print("| o o |")
        print("-------")
    elif X == 5:
        print("-------")
        print("|o   o|")
        print("|  o  |")
        print("|o   o|")
        print("-------")
    else:
        print("-------")
        print("| o o |")
        print("| o o |")
        print("| o o |")
        print("-------")
        

    p = input("press y to role again: ")
