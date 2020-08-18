# crazy_eights.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

from cards import Card
import random

def init_cards():
    global deck, p_hand, c_hand, up_card, active_suit, active_rank
    deck = []
    for suit in range(1, 5):
        for rank in range(1, 14):
            new_card = Card(suit, rank)
            # Make eights worth 50 points
            if new_card.rank == 8:
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

def player_turn():
    global deck, p_hand, blocked, up_card, active_suit
    valid_play = False
    is_eight = False
    print("\nYour hand:  ", end='')
    for card in p_hand:
        print(card.short_name, end=' ')
    print("   Up card: ", up_card.short_name)
    if up_card.rank == '8':
        print("   Suit is", active_suit)
    print("What would you like to do?  ", end='')
    response = input("Type a card to play or 'Draw' to take a card: " )
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
    p_hand.remove(selected_card)
    up_card  = selected_card
    if is_eight:
        get_new_suit()
    else:
        active_suit = up_card.suit
    print("You played", selected_card.short_name)

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

done = False
p_total = c_total = 0
while not done:
    game_done = False

    blocked = 0
    init_cards()  # Sets up deck and player and computer hands
    while not game_done:
        player_turn()
        if len(p_hand) == 0:  # Player wins
            game_done = True
            print()
            print("You won!")
            # display game score here
            p_points = 0

            # Adds points from computer’s remaining cards
            for card in c_hand:
                p_points += card.value
            p_total += p_points  # Adds points from this game to total
            print("You got %i points for computer's hand" % p_points)

        if not game_done:
            computer_turn()
        if len(c_hand) == 0:  # Computer wins
            game_done = True
            print()
            print("Computer won!")
            # display game score here
            c_points = 0
            # Adds points from player’s remaining cards
            for card in p_hand:
                c_points += card.value
            c_total += c_points  # Adds points from this game to total
            print("Computer got %i points for your hand" % c_points)
        if blocked >= 2:
            # Both blocked, so both get points
            game_done = True
            print("Both players blocked.  GAME OVER.")
            player_points = 0
            for card in c_hand:
                p_points += card.value
            p_total += p_points
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points
            # Prints game points
            print("You got %i points for computer's hand" % p_points)
            print("Computer got %i points for your hand" % c_points)
    play_again = input("Play again (Y/N)? ")
    if play_again.lower().startswith('y'):
        done = False
        # Prints total points so far
        print("\nSo far, you have %i points" % p_total)
        print("and the computer has %i points.\n" % c_total)
    else:
        done = True

# Prints final totals
print("\n Final Score:")
print("You: %i     Computer: %i" % (p_total, c_total))
