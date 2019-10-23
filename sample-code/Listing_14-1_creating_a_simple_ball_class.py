# Listing_14-1_creating_a_simple_ball_class.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

class Ball:  # This tells Python we’re making a class.

    # This is a method.
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"
