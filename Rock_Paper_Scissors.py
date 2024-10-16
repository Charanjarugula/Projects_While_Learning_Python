import random

Rounds = 0
Wins = 0
Losses = 0

def play_round():
    global Wins, Losses
    Choice = input('(R)ock, (P)aper, or (S)cissors? ').upper()
    my_list = ["R", "P", "S"]
    Answer = random.choice(my_list)
    print("I chose " + Answer + "!")

    if (Choice == "P" and Answer == "R") or (Choice == "S" and Answer == "P") or (Choice == "R" and Answer == "S"):
        print("You Win!")
        Wins += 1
    elif Choice == Answer:
        print("It's a Tie!")
    else:
        print("You Lose!")
        Losses += 1

print("Let's play rock-paper-scissors!")

while Rounds < 3:
    play_round()
    Rounds += 1
    print(str(Wins) + " - " + str(Losses))

    if Rounds == 3:
        print("Game over!")
        print(str(Wins) + " - " + str(Losses))
    else:
        if Rounds == 1:
            Input = input("Best of three? (Y)es or (N)o ").upper()
            if Input == 'N':
                print("Thanks for playing!")
                break
