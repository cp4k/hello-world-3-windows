# Listing_23-6_creating_cards_for_crazy_eights.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

def init_cards():
    global deck, p_hand, c_hand, up_card, active_suit, active_rank
    deck = []
    for suit in range(1, 5):
        for rank in range(1, 14):
            new_card = Card(suit, rank)
            # Make eights worth 50 points
            if new_card.rank == 8:  # Make eights worth 50 points
                new_card.value = 50
            deck.append(new_card)
    p_hand = []
    c_hand = []
    for i in range(5):
        p_card = random.choice(deck)
        deck.remove(p_card)
        p_hand.append(p_card)
        c_card = random.choice(deck)
        deck.remove(c_card)
        c_hand.append(c_card)
    up_card = random.choice(deck)
    deck.remove(up_card)
    active_suit = up_card.suit
    active_rank = up_card.rank
