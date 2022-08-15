def play():
    print("✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎")
    print("✝✝✝Welcome to Hangman Game!✝︎✝︎✝︎")
    print("✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝✝︎✝︎✝︎✝︎")

    secret_word = "banana"

    wrong = False
    right = False

    while(not wrong and not right):

        shot = input("Type a letter...")
        shot = shot.strip()

        index = 0
        for letter in secret_word:
            if(shot.upper() == letter.upper()):
                print("Find the letter {} on the position {}".format(letter, index))
            index = index + 1    

        print("playing...")

    print("Game Over")

if(__name__ == "__main__"):
    play()    