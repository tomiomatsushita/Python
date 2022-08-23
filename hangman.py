def play():
    print("✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎")
    print("✝✝✝Welcome to Hangman Game!✝︎✝︎✝︎")
    print("✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝✝︎✝︎✝︎✝︎")

    secret_word = "banana".upper()
    hit_letter = ["_" for letter in ]

    # To make the code more readable,
    # the lines of code below have been 
    # replaced by a command defined on just one line
    # which can be seen above in the hit_letter variable 
    # with the feature of list List Comprehension
    # for letter in secret_word:
    #    hit_letter.append("_")

    wrong = False
    right = False
    trys = 0

    print(hit_letter)

    while(not wrong and not right):

        shot = input("Type a letter...")
        shot = shot.strip().upper()

        if(shot in secret_word):
            index = 0
            for letter in secret_word:
                if(shot == letter):
                    hit_letter[index] = letter
                index += 1    
        else:
            trys += 1

        wrong = trys == 6
        right = "_" not in hit_letter
        print(hit_letter)
    if(right):
        print("Congratulations, you win!")
    else:    
        print("You exceeded the number of attempts!")
        print("☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️")
        print("☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️Game Over☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️")
        print("☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️")

if(__name__ == "__main__"):
    play()    