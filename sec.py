import random
number = random.randint(1,9)
chances = 0
while chances < 5:
    enternum = int(input("enter the number: "))
    if enternum == number:
        print("that is the right number")
        break
    elif enternum < number:
        print("guess higher")
    else:
        print("guess lower")

    chances = chances + 1

if not chances < 5:
    print("you have lost")
    print("the number was: " , number)