#gissa talet
import time
from random import randint
wann_play = input("""wanna play?(Yes, No) :
""")
try:
    wanna_play = str(wann_play.lower())
except ValueError:
    print("Idiot, det där var varken Ja eller nej utan ett tal! Här får inte idioter vara!!!")
    time.sleep(5.0)
    quit()


while wanna_play == "yes":
    game_on = True
    turn = 0
    secret_number = randint(0, 100)
    while game_on:

        try:
            guess = int(input("""guess the number:"""))

        except ValueError:
            print("Idiot, det där var inte ett tal. Du får en chans till.")
            break

        if guess < secret_number:
            print("Too Small")
            turn += 1

        elif guess == secret_number:
            print("thats right")
            play = True
            turn += 1
            print("You win! Your total turns to guess the right number was ", turn, " !")
            while play == True:

                pla_again = str(input("""want to play again?(Yes, No):
                """))
                play_again = pla_again.lower()
                if play_again == "yes":
                    game_on = False
                    play = False
                elif play_again == "no":
                    game_on = False
                    wanna_play = "no"
                    play = False
                else:
                    print("that is not an option")



        elif guess > secret_number:
            print("Too Big")
            turn += 1
        else:
            print("that is not an option")
if wanna_play == "no":
    print("that is sad")
if wanna_play is not "no" or "yes":
    print("du är en idiot som inte kan följa instructioner, Gå här ifrån eller försök igen!!!!!!!!")
time.sleep(2.0)
quit()