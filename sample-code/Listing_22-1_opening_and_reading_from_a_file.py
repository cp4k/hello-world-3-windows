# Listing_22-1_opening_and_reading_from_a_file.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

my_file = open('notes.txt', 'r')
lines = my_file.readlines()
print(lines)
