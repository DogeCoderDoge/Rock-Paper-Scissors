#Rock, Paper, Scissors

print("Welcome to Rock, Paper, Scissors")
play = input("Type PLAY to continue:  ")
play.casefold()

if play == "play":
    game_live = True

    while game_live:
        print("Rock, Paper or Scissors? EXIT to EXIT")
        choice = input()
        choice.casefold()

        if choice != "EXIT":
            #Creating a choice generator
            import random
            compChoices = ["Rock", "Paper", "Scissors"]
            compNum = random.randint(0, 2)

            print("Comp picked", compChoices[compNum])
            comp = compChoices[compNum]


            #Checking for winner/loser
            if choice == "rock" and comp == "Scissors":
                print("You win")

            elif choice == "paper" and comp == "Rock":
                print("You win")    

            elif choice == "scissors" and comp == "Paper":
                print("You win")

            elif choice == "rock" and comp == "Paper":
                print("You lose")

            elif choice == "paper" and comp == "Scissors":
                print("You lose")

            elif choice == "scissors" and comp == "Rock":
                print("You lose")

            else: print("Tie") 

        else:
            print("Thank you for playing!")
            game_live = False

else: print(":/")