import random #random is a library to generate random numbers

number=random.randrange(1,10)


def guess():

    print("Welcome to number guessing game!!!")
    print("You have 6 chances")
    print("------------------------------")
    choice = int(input("Guess a number b/w (1,10):"))
    print("------------------------------")

    chance = 0

    while chance < 6:

        if choice < number:
            print("Your guess was low")
            choice = int(input("Guess a number b/w (1,10):"))

        elif choice > number:
            print("Your guess was higer")
            choice = int(input("Guess a number b/w (1,10):"))

        elif choice == number:
            
            print()
            print(f"Great, You've Won !!!!, congrats, the answer is {number}")

            break

        chance +=1


        if chance == 6:
            print(f"your chance has been completed, the answer is {number}")

guess()
