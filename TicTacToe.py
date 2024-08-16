import random

#Main game function
def main():
    while True:
        print("Welcome to the dangerous game of Tic Tac Toe")
        print("--------------------------------------------")

        #The number choices to pick from the game board
        possibleNumbers = [1,2,3,4,5,6,7,8,9]
        gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
        rows = 3
        cols = 3

        #Function to create the tic tac toe board
        def printGameBoard():
            for x in range(rows):
                print("\n+---+---+---+")
                print("|", end="")
                for y in range (cols):
                    print("", gameBoard[x][y], end=" |")
            print("\n+---+---+---+")

        #Function to change the array to the CPU's or user's choice
        def modifyArray(num, turn):
            num -= 1

            if(num == 0):
                gameBoard[0][0] = turn
            elif(num == 1):
                gameBoard[0][1] = turn
            elif(num == 2):
                gameBoard[0][2] = turn
            elif(num == 3):
                gameBoard[1][0] = turn
            elif(num == 4):
                gameBoard[1][1] = turn
            elif(num == 5):
                gameBoard[1][2] = turn
            elif(num == 6):
                gameBoard[2][0] = turn
            elif(num == 7):
                gameBoard[2][1] = turn
            elif(num == 8):
                gameBoard[2][2] = turn

        #Function to check for the winner
        def checkForWinner(gameBoard):
            win_conditions = [
                [gameBoard[0][0], gameBoard[0][1], gameBoard[0][2]],
                [gameBoard[1][0], gameBoard[1][1], gameBoard[1][2]],
                [gameBoard[2][0], gameBoard[2][1], gameBoard[2][2]],
                [gameBoard[0][0], gameBoard[1][0], gameBoard[2][0]],
                [gameBoard[0][1], gameBoard[1][1], gameBoard[2][1]],
                [gameBoard[0][2], gameBoard[1][2], gameBoard[2][2]],
                [gameBoard[0][0], gameBoard[1][1], gameBoard[2][2]],
                [gameBoard[2][0], gameBoard[1][1], gameBoard[0][2]]
            ]
            #Check if the conditions are met
            for condition in win_conditions:
                if condition[0] == condition[1] == condition[2]:
                    print(f"{condition[0]} has won!")
                    return True
            return False
                
        #Function to run the game
        def gameRun():
            game_over = False
            turnCounter = 0
            while not game_over:
                if(turnCounter % 2 == 1):
                    printGameBoard()
                    numberPicked = int(input("\nChoose a number [1-9]: "))
                    if numberPicked in possibleNumbers:
                        modifyArray(numberPicked, 'X')
                        possibleNumbers.remove(numberPicked)
                        if checkForWinner(gameBoard):
                            printGameBoard()
                            game_over = True
                        turnCounter += 1
                    else:
                        print("Invalid input. Number already chosen or out of range. Please enter a number between 1 and 9.")            
                else: #CPU's choices
                    while(True):
                        cpuChoice = random.choice(possibleNumbers)
                        print("\nCpu choice: ", cpuChoice)
                        if cpuChoice in possibleNumbers:
                            modifyArray(cpuChoice, 'O')
                            possibleNumbers.remove(cpuChoice)
                            if checkForWinner(gameBoard):
                                printGameBoard()
                                game_over = True
                            turnCounter += 1
                            break
                if len(possibleNumbers) == 0 and not game_over:
                    print("It's a draw!")
                    break
        #Run the game
        gameRun()
        #Asks if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
