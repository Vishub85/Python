#guess the number
import random
name = input("Enter player name: ")
num = int(input("Enter a number between 1 and 9: "))
if 1 <= num <= 9:
    r_num = random.randint(1, 9)
    print(name,"you entered:",num)
    print("Computer selected:",r_num)
    if num == r_num:
        print(name,"your guess is Correct.")
    else:
        print(name,"your guess is Incorrect. Try again.")
else:
    print("Invalid number. Try again.")
