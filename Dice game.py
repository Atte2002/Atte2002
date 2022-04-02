import random
import time

again = "y"

while again == "y":

    if again == "n":
        break


    player1_score = 0
    player2_score = 0

    rolls = int(input("How many times would you like to roll the dice?: "))
    print("")

    for i in range(rolls):

        player1_value = random.randint(1,6)
        player2_value = random.randint(1,6)

        print("Player 1 rolled: " + str(player1_value))
        print("Player 2 rolled: " + str(player2_value))

        if player1_value > player2_value:
            print("Player 1 wins!")
            print("")
            player1_score = player1_score + 1
            time.sleep(1)
    
        elif player1_value < player2_value:
            print("Player 2 wins!")
            print("")
            player2_score = player2_score + 1
            time.sleep(1)

        else:
            print("It's a draw, no one gets a point!")
            print("")
            time.sleep(1)

    print("Game over!")

    if player1_score > player2_score:
        print("Player 1 wins the tournament! " + str(player1_score) + " to " + str(player2_score))
        print("")
    
    elif player1_score < player2_score:
        print("Player 2 wins the tournament! " + str(player2_score) + " to " + str(player1_score))
        print("")

    else:
        print("The tournament was a draw! " + str(player1_score) + " to " + str(player2_score))
        print("")

    again = ""

    while again != "y" and again != "n":

        again = input("Would you like to play again? Type y to continue, n to stop the game: ")
        if again != "y" and again != "n":
            print("Invalid command, try again... ")
            print("")

 