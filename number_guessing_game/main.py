import random #random is a library to generate random numbers

number=random.randrange(1,10)

chance = 0
print("Welcome to number guessing game!!!")
print("You have 6 chances")
print("------------------------------")
choice = int(input("Guess a number b/w (1,10):"))

print("------------------------------")

while chance < 6:

    if choice < number:
        print("Your guess was low")
        choice = int(input("Guess a number b/w (1,10):"))

    elif choice > number:
        print("Your guess was higer")
        choice = int(input("Guess a number b/w (1,10):"))

    elif choice == number:
        print(f"Great, You've Won !!!!, congrats, the answer is {number}")

        break

    chance +=1


    if chance == 6:
        print(f"your chance has been completed, the answer is {number}")
