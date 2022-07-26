print("Welcome to Guess a Number")

secret_number = 46
try_times = 5
round = 1

while(round <= try_times):
    print("Try {} of {}".format(round, try_times))
    shot_str= input("Enter a number: ")
    print("You type:" , shot_str)
    shot = int(shot_str)

    win = shot == secret_number
    higher = shot > secret_number
    lower = shot < secret_number 

    if(win):
        print("You win! Congrats")
    else:
        if(higher):
            print("You are wrong! The number entered is higher than the secret number.")
        elif(lower):
            print("You are wrong! The number entered is lower than the secret number.")

    round = round + 1

print("Game Over")            