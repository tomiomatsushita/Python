import random

print("Welcome to Guess a Number")

#to generate a random number the function random() will be import and include
#the function random.randrange will generate a random integer number  

secret_number = random.randrange(1, 101)
try_times = 5
score = 1000

print("Select you level")
print("(1) Easy (2) Medium (3) Hard")

level = int(input("Chosen Level:"))

if(level == 1):
    try_times = 20
elif(level == 2):
    try_times = 10
else:
    try_times = 5        

#to improve code readability and also make it cleaner. Implemented a for instead of while to create a loop.
for round in range(1, try_times + 1):
    print("Try {} of {}".format(round, try_times))
    shot_str= input("Enter a number between 1 and 100: ")
    print("You type:" , shot_str)
    shot = int(shot_str)

    if(shot < 1 or shot > 100):
        print("The number entered is invalid!")
        continue

    win = shot == secret_number
    higher = shot > secret_number
    lower = shot < secret_number 

    if(win):
        print("You win! Congrats! Your Score is {}".format(score))
        break
    else:
        if(higher):
            print("You are wrong! The number entered is higher than the secret number.")
        elif(lower):
            print("You are wrong! The number entered is lower than the secret number.")
        lost_score = abs(secret_number - shot)
        score = score - lost_score

print("Game Over")            