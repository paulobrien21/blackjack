import random
#function calls 2 variable. First variable = requested number of cards in generated deck.
    #Second variable: True returns deck as list. False(default) returns deck as dictionary with each card assigned value (Two of Hearts: 2, Queen of Diamonds: 10 etc)
def deck_generator(num_of_cards = 52, check = False):

    deck_count = [  'Ace of ', 'Two of ', 'Three of ', 'Four of ',
                    'Five of ', 'Six of ', 'Seven of ', 'Eight of ', 'Nine of ',
                    'Ten of ', 'Jack of ', 'King of ', 'Queen of ']

    deck_suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    new_deck = {}

    value = 1

    #Create dictionary to assign integer values to cards using combinations of deck_suit & deck_count as keys
    for i in deck_count:
        x = 0
        while x < 4:
            suit = deck_suit[x]
            new_card = i + suit
            new_deck.update({new_card: value})
            x += 1

        if value < 10:
            value += 1

    #Shuffle deck by assigning key/value pairs as tuples in a new list, shuffle list before assigning new order back to original dictionary
    temp_list = list(new_deck.items())
    random.shuffle(temp_list)
    # if user does not want full deck (passed variable is less than 52) loop i number of times and remove 1 card per loop (i = full deck - number of cards requested)
    if num_of_cards != 52:
        for i in range(52 - num_of_cards):
            temp_list.pop()
    #reconstruct deck into dictionary
    new_deck = dict(temp_list)

    #if user wants just the keys(string card names) and not the values assigned to each card, we create a new deck list with just the keys
    if check == True:
        list_deck = []
        for i in new_deck.keys():
            list_deck.append(i)
        return list_deck

    #else return deck (keys + values)
    else:
        return new_deck