import hangman
import guess_the_number

def choose_game():
    print("***********************")
    print("******Welcome!*********")
    print("****Choose a game******")
    print("***********************")

    print("(1) hangman (2) Guess a Number")

    game = int(input("Wich game you choose?"))

    if(game == 1):
        print("Playing hangman")
        hangman.play()
    elif(game == 2):
        print("Playing Guess a Number")
        guess_the_number.play()

if(__name__ == "__main__"):
    choose_game()    
