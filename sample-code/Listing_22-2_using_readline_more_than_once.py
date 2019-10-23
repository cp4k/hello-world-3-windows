# Listing_22-2_using_readline_more_than_once.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

my_file = open('notes.txt', 'r')
first_line = my_file.readline()
second_line = my_file.readline()
print("first line = ", first_line)
print("second line = ", second_line)
my_file.close()
