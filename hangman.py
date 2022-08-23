import random

def play():
    print("✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎")
    print("✝✝✝Welcome to Hangman Game!✝︎✝︎✝︎")
    print("✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝✝︎✝︎✝︎✝︎")

    # add a text file with a list of words
    # to use it for generate random words

    file = open("words_for_hangman_game.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0,len(words))
    secret_word = words[number].upper()    
    hit_letter = ["_" for letter in secret_word]

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