# Listing_23-9_getting_the_players_choice.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

print("What would you like to do?  ", end='')
response = input("Type a card to play or 'Draw' to take a card: " )
valid_play = False
while not valid_play:  # Keeps trying until player enters something valid
    selected_card = None
    # Gets a card the player has in hand, or draws
    while selected_card == None:
        if response.lower() == 'draw':
            valid_play = True
            if len(deck) > 0:
                # If “draw”, takes card from deck and adds it to player’s hand
                card = random.choice(deck)
                p_hand.append(card)
                deck.remove(card)
                print("You drew", card.short_name)
            else:
                print("There are no cards left in the deck")
                blocked += 1
            return  # Got “draw”, so returns to main loop
        else:
            for card in p_hand:
                if response.upper() == card.short_name:  # Checks if the selected card is in player’s hand—keeps trying until it is (or he draws)
                    selected_card = card
            if selected_card == None:
                response = input("You don't have that card. Try again:")

    if selected_card.rank == '8':  # Playing an 8 is always legal
        valid_play = True
        is_eight = True
    elif selected_card.suit  == active_suit:  # Checks if selected card matches up-card suit
        valid_play = True
    elif selected_card.rank  == up_card.rank:  # Checks if selected card matches up-card rank
        valid_play = True

    if not valid_play:
        response = input("That's not a legal play.  Try again: ")
