# Listing_6-3_getting_input_using_an_enter_box.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?")
easygui.msgbox("You entered " + flavor)
