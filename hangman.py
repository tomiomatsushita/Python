def play():
    print("✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎")
    print("✝✝✝Welcome to Hangman Game!✝︎✝︎✝︎")
    print("✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝︎✝✝︎✝︎✝︎✝︎")

    secret_word = "banana"
    hits_letters = ["_","_","_","_","_","_"]

    wrong = False
    right = False

    print(hits_letters)

    while(not wrong and not right):

        shot = input("Type a letter...")
        shot = shot.strip()

        index = 0
        for letter in secret_word:
            if(shot.upper() == letter.upper()):
                hits_letters[index] = letter
            index = index + 1    

        print(hits_letters)

    print("Game Over")

if(__name__ == "__main__"):
    play()    