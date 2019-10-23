# Listing_23-8_displaying_whats_in_the_players_hand.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

print("\nYour hand:  ", end='')
for card in p_hand:
    print(card.short_name, end=' ')
print("   Up card: ", up_card.short_name)
if up_card.rank == '8':
    print("   Suit is", active_suit)
