# Listing_23-11_the_computers_turn.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

def computer_turn():
    global c_hand, deck, up_card, active_suit, blocked
    options = []
    for card in c_hand:
        if card.rank == '8':  # Plays an 8
            c_hand.remove(card)
            up_card = card
            print("  Computer played ", card.short_name)
            #suit totals:  [diamonds, hearts, spades, clubs]
            suit_totals = [0, 0, 0, 0]  # Counts cards in each suit; suit with the most is the “long suit”
            for suit in range(1, 5):
                for card in c_hand:
                    if card.suit_id == suit:
                        suit_totals[suit-1] += 1
            long_suit = 0
            for i in range (4):
                if suit_totals[i] > long_suit:
                    long_suit = i
            # Makes long suit the active suit
            if long_suit == 0:  active_suit = "Diamonds"
            if long_suit == 1:  active_suit = "Hearts"
            if long_suit == 2:  active_suit = "Spades"
            if long_suit == 3:  active_suit = "Clubs"
            print("  Computer changed suit to ", active_suit)
            return  # Ends computer’s turn; back to main loop
        else:
            # Checks what cards are possible plays
            if card.suit == active_suit:
                options.append(card)
            elif card.rank == up_card.rank:
                options.append(card)

    if len(options) > 0:
        best_play = options[0]
        # Checks which option is best (highest value)
        for card in options:
            if card.value > best_play.value:
                best_play = card

        # Plays card
        c_hand.remove(best_play)
        up_card = best_play
        active_suit = up_card.suit
        print("  Computer played ", best_play.short_name)


    else:
        if len(deck) > 0:
            # Draws, because no possible plays
            next_card = random.choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
            print("  Computer drew a card")
        else:
            # No cards left in deck—computer is blocked
            print("  Computer is blocked")
            blocked += 1
    print("Computer has %i cards left" % (len(c_hand)))
