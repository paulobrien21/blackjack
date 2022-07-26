import cards, time, random


def draw_cards(deck, hand, draw_num):

    for i in range(draw_num):
        temp_deck = list(deck.keys())
        temp_card = temp_deck.pop(random.randint(0, len(temp_deck)-1))
        value = deck.pop(temp_card)
        hand[temp_card] = value

    return hand, deck


def ace_check(hand, ace_control = False):

    if ace_control == False:
        for i in hand:
            if 'Ace' in i:
                hand[i] = 11
                ace_control = True
                break

    else:
        for i in hand:
            if 'Ace' in i:
                hand[i] = 1

    return hand, ace_control


play = input("Do you want to play Blackjack? Y/N: ").upper()

while play == "Y":

    # Generate deck from the imported cards module(passing 52 as number of cards required in deck ie a full deck)
    deck = cards.deck_generator(52)
    player_hand = {}
    dealer_hand = {}
    ace_control = False

    #draw cards for dealer and player to start the game using draw_cards function (passing the current deck, hand to draw for & number of cards to draw for that hand)
    player_hand, deck = draw_cards(deck, player_hand, 2)
    dealer_hand, deck = draw_cards(deck, dealer_hand, 1)

    #in blackjack, ace can be 1 or 11 depending on circumstance. ace_check() is used to turn an ace from 1 to 11 or vice versa and ace_control tracks if an ace has already been transformed
    player_hand, ace_control = ace_check(player_hand)
    if ace_control == True:
        dealer_hand, ace_control = ace_check(dealer_hand)
        ace_control = True
    else:
        dealer_hand, ace_control = ace_check(dealer_hand)

    print("Dealing cards....")
    print("")
    time.sleep(2)

    #calculate player and dealer score and display along with player and dealers current hands
    player_score = sum(player_hand.values())
    dealer_score = sum(dealer_hand.values())
    print(f"Your Hand: {player_hand} | Your score: {player_score}")
    print(f"Dealer's Hand: {dealer_hand} | Dealer Score: {dealer_score}")

    #player turn
    #Player can choose to Hold(H) or Draw(D). Loop breaks when player decides to Hold or their score goes above 21
    action = ''
    while player_score < 21 and len(player_hand) < 5 and action != 'H':
        print("")
        action = input("Draw or Hold? D/H: ").upper()
        print("")
        time.sleep(1)
        if action == 'D':
            player_hand, deck = draw_cards(deck, player_hand, 1)
            if ace_control == False:
                player_hand, ace_control = ace_check(player_hand, ace_control)
            player_score = sum(player_hand.values())
            if player_score > 21 and ace_control == True:
                player_hand, ace_control = ace_check(player_hand, ace_control)
                player_score = sum(player_hand.values())
            print(f"Your Hand: {player_hand} | Your score: {player_score}")
            print(f"Dealer's Hand: {dealer_hand} | Dealer Score: {dealer_score}")

    #checking outcome after player's turn depending on score
    if player_score > 21:
        print("BUST! You've gone over 21...you lose... :(")
    elif len(player_hand) == 5:
        print("You hold 5 cards and you're still 21 or under...you win! :)")
    elif player_score <= dealer_score:
        if player_score < dealer_score:
            print("Oops! Looks like the dealer has won already...")
        else:
            print("Dealer has settled for the draw...")

    #if player hasnt won, drawn or bust, now it's the dealer's turn to draw
    else:
        if player_score == 21:
            print("You got 21!")
            print("")
        #dealer turn
        dealer_hand, ace_control = ace_check(dealer_hand)
        while dealer_score <= 21 and dealer_score < player_score:
            print("")
            print("Dealer thinking.......")
            time.sleep(2)
            dealer_hand, deck = draw_cards(deck, dealer_hand, 1)
            if ace_control == False:
                dealer_hand, ace_control = ace_check(dealer_hand, ace_control)
            dealer_score = sum(dealer_hand.values())
            if dealer_score > 21 and ace_control == True:
                dealer_hand, ace_control = ace_check(dealer_hand, ace_control)
                dealer_score = sum(dealer_hand.values())
            print(f"Your Hand: {player_hand} | Your score: {player_score}")
            print(f"Dealer's Hand: {dealer_hand} | Dealer Score: {dealer_score}")
            time.sleep(2)

        #checking if dealer bust and if not, comparing to player's score to judge winner
        if dealer_score > 21:
            print("Dealer Bust! You win! :)")
        elif dealer_score == player_score:
            print("Dealer has settled for the draw...")
        else:
            print("Dealer wins!.. :(")

    time.sleep(2)
    #game is finished and user can decide to play again or end program
    play = input("Do you want to play again? Y/N: ").upper()
