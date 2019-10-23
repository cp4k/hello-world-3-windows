# Listing_8-8_a_conditional_or_while_loop.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

print("Type 3 to continue, anything else to quit.")
someInput = input()
while someInput == '3':  # Keep looping as long as `someInput` is 3
    # Body of the loop
    print("Thank you for the 3.  Very kind of you.")
    print("Type 3 to continue, anything else to quit.")
    someInput = input()
print("That's not 3, so I'm quitting now.")
