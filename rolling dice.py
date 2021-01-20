import random

min = 1
max = 6
while True:
    print("welcome to rolling dices!!!!! \n do wanna roll dices ??? \n  >>>> yes or no ????")
    answer = str(input())
    if answer.lower() == "yes" or answer.lower() == "y":
        print("okay !!!! here is your lucky nums >>>",random.randint(min,max),",",random.randint(min,max))


    elif answer.lower() == "no" or answer.lower() == "n":
        print("okay thank you ")
        break
