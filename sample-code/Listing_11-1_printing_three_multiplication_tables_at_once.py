# Listing_11-1_printing_three_multiplication_tables_at_once.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

# This outer loop runs 3 iterations with the values 5, 6, 7
for multiplier in range(5, 8):
    # This inner loop prints a single table
    for i in range(1, 11):
        print(i, "x", multiplier, "=", i * multiplier)
    print()
