# Listing_23-10_getting_the_new_suit_when_the_player_plays_an_8.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

def get_new_suit():
    global active_suit
    got_suit = False
    while not got_suit:  # Keeps trying until player enters a valid suit
        suit = input("Pick a suit: ")
        if suit.lower() == 'd':
            active_suit = "Diamonds"
            got_suit = True
        elif suit.lower() == 's':
            active_suit = "Spades"
            got_suit = True
        elif suit.lower() == 'h':
            active_suit = "Hearts"
            got_suit = True
        elif suit.lower() == 'c':
            active_suit = "Clubs"
            got_suit = True
        else:
            print("Not a valid suit.  Try again. ", end='')
    print("You picked", active_suit)
