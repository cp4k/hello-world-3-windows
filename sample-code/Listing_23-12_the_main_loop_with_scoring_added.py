# Listing_23-12_the_main_loop_with_scoring_added.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

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
