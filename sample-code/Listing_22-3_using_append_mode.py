# Listing_22-3_using_append_mode.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

todo_list = open('notes.txt', 'a')  # Opens the file in append mode
todo_list.write('\nSpend allowance')  # Adds our string to the end
todo_list.close()  # Closes the file
