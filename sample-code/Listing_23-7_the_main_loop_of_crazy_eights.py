# Listing_23-7_the_main_loop_of_crazy_eights.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

game_done = False
init_cards()
while not game_done:
    blocked = 0
    player_turn()  # Player’s turn
    if len(p_hand) == 0:  # Player’s hand (`p_hand`) has no cards left, so player wins
       game_done = True
       print()
       print("You won!")
    if not game_done:
       computer_turn()  # Computer’s turn
    if len(c_hand) == 0:  # Computer’s hand (`c_hand`) has no cards left, so computer wins
       game_done = True
       print()
       print("Computer won!")
    if blocked >= 2:  # Both players are blocked, so game ends
       game_done = True
       print("Both players blocked.  GAME OVER.")
