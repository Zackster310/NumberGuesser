import random

number = random.randint(1, 20)
chances = 5

while chances > 0:
    userNumber = int(input("guess the number: "))

    if userNumber == number:
        print ("You Win!!!")
        break

    elif userNumber > number:
        print ("Your number is too high")

    elif userNumber < number:
        print ("Your number is too low")

    chances = chances - 1

if chances == 0:
    print ("You have used all your chances, you lose!")