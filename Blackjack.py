import random

#Function to run the Blackjack game
def play_blackjack():
    playerIn = True
    dealerIn = True

#An array with the different card values
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
    playerHand = []
    dealerHand = []

#Function to randomly select cards for the dealer and player
    def dealCard(turn):
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)

#Calculations for each card
    def total(turn):
        total = 0
        aces = 0
        face = ['J', 'Q', 'K']
        for card in turn:
            if card in range(1, 11):
                total += card
            elif card in face:
                total += 10
            else:
                total += 11
                aces += 1
    
        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total
    
    #Function to reveal the dealer's hands
    def revealDealerHand():
        if len(dealerHand) == 2:
            return dealerHand[0]
        elif len(dealerHand) > 2:
            return dealerHand[0], dealerHand[1]
        
    #Cards are dealt to the dealer and player
    for _ in range(2):
        dealCard(dealerHand)
        dealCard(playerHand)

    #Main
    while playerIn or dealerIn:
        print(f"Dealer had {revealDealerHand()} and X")
        print(f"You have {playerHand} for a total of {total(playerHand)}")
        if playerIn:
            stayOrHit = input("Would you like to stay or hit? ").lower()
            
            if stayOrHit == 'stay':
                playerIn = False
            elif stayOrHit == 'hit':
                dealCard(playerHand)
            else:
                print("Invalid input. Please type 'stay' or 'hit'.")
                continue

        #If the dealer has 16 or less, it has to hit
        if total(dealerHand) > 16:
            dealerIn = False
        else:
            dealCard(dealerHand)

        #If the total of the cards is 21 or over, it breaks
        if total(playerHand) >= 21:
            break
        elif total(dealerHand) >= 21:
            break

    #Different outcomes
    if total(playerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack! You win!")
    elif total(dealerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack! Dealer wins!")
    elif total(playerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You bust! Dealer wins!")
    elif total(dealerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Dealer busts! You win!")
    elif total(dealerHand) < total(playerHand) and total(playerHand)<= 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You are closer to 21! You win!")
    elif total(playerHand) < total(dealerHand) and total(dealerHand)<= 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("The dealer is closer to 21! Dealer wins!")

#Option to play again
while True:
    play_blackjack()
    replay = input("Do you want to play again? Type 'yes' to play again or 'no' to exit: ").lower()
    if replay != 'yes':
        break

print("Thanks for playing!")
