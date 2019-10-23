# Listing_23-3_looking_for_10_heads_in_a_row.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

from random import *
coin = ["Heads", "Tails"]
heads_in_row = 0
ten_heads_in_row = 0
for i in range (1000000):
    if choice(coin) == "Heads":  # Flips the coin
        heads_in_row += 1
    else:
        heads_in_row = 0
    if heads_in_row == 10:
        ten_heads_in_row += 1  # Got 10 heads in a row, increments counter
        heads_in_row = 0

print("We got 10 heads in a row", ten_heads_in_row, "times.")
