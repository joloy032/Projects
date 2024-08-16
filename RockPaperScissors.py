import random

#The different options to choose from
options = ("rock", "paper", "scissors")
#Keeping the game running
running = True

#Main loop
while running:

    #Currently what the player and computer has
    player = None
    computer = random.choice(options)

    #User chooses rock, paper, or scissors
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
        if player not in options:
            print("That isn't one of the options.")

    #Prints the player's and computer's action
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    #Different outcomes of the game
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors" or player == "scissors" and computer == "paper" or player == "paper" and computer == "rock":
        print("You win!")
    else:
        print("You lose!")

    #Option to play again
    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False

print("Have a splendid day!")
