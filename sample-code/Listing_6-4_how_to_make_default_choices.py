# Listing_6-4_how_to_make_default_choices.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                           default = 'Vanilla')  # Here’s the default
easygui.msgbox("You entered " + flavor)
