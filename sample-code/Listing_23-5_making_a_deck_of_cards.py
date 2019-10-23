# Listing_23-5_making_a_deck_of_cards.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import random
from cards import Card  # Imports our `cards` module

deck = []
# Uses nested `for` loops to make a deck
for suit_id in range(1, 5):
    for rank_id in range(1, 14):
        deck.append(Card(suit_id, rank_id))

# Picks 5 cards from the deck to make a hand
hand = []
for cards in range(0, 5):
    a = random.choice(deck)
    hand.append(a)
    deck.remove(a)

print()
for card in hand:
    print(card.short_name, '=' ,card.long_name, "  Value:", card.value)
