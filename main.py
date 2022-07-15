import cards
import time

def player_turn():
    pass

def dealer_turn():
    pass

#Generate deck from the imported cards module(passing 52 as number of cards required in deck ie a full deck)
deck = cards.deck_generator(52)

play = input("Do you want to play Blackjack? Y/N: ").upper()

while play == "Y":
    player_hand = {}
    dealer_hand = {}
    print("Dealing cards....")
    time.sleep(1)

    player_score, deck = player_turn(deck, player_hand, dealer_hand)
    pass