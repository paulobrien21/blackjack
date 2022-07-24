import cards
import time
import random


def draw_cards(deck, hand, draw_num):

    for i in range(draw_num):
        temp_deck = list(deck.keys())
        print(temp_deck)
        temp_card = temp_deck.pop(random.randint(0, len(temp_deck)-1))
        print(temp_card)
        value = deck.pop(temp_card)
        print(value)
        hand[temp_card] = value
        print(hand)

    return hand, deck


#Generate deck from the imported cards module(passing 52 as number of cards required in deck ie a full deck)

deck = cards.deck_generator(52)

play = input("Do you want to play Blackjack? Y/N: ").upper()

while play == "Y":
    player_hand = {}
    dealer_hand = {}
    #draw cards for dealer and player to start the game using draw_cards function (passing the current deck, hand to draw for & number of cards to draw for that hand)
    player_hand, deck = draw_cards(deck, player_hand, 2)
    dealer_hand, deck = draw_cards(deck, dealer_hand, 2)
    print("Dealing cards....")
    time.sleep(2)
    print(player_hand)
    print(dealer_hand)

    #player turn
    player_score = 0
    action = ''
    while player_score <= 21 and action != 'H':
        action = input("Draw or Hold? D/H: ").upper()
        if action == 'D':
            player_hand, deck = draw_cards(deck, player_hand, 1)

    #dealer turn
    dealer_score = 0
    while dealer_score <= 21 and dealer_score < player_score:
        dealer_hand, deck = draw_cards(deck, dealer_hand, 1)

    play = input("Do you want to play again? Y/N: ")
