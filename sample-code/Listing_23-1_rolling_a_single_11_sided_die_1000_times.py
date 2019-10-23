# Listing_23-1_rolling_a_single_11_sided_die_1000_times.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import random

totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # List has 13 items, with index 0 to 12
for i in range(1000):
    dice_total = random.randint(2, 12)
    totals[dice_total] += 1  # Adds 1 to the count of this total

for i in range (2, 13):
    print("total", i, "came up", totals[i], "times")
