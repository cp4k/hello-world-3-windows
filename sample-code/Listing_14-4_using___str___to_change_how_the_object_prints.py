# Listing_14-4_using___str___to_change_how_the_object_prints.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    # Here’s the `\\__str__()` method.
    def __str__(self):
        msg = "Hi, I'm a " + self.size + " " + self.color + " ball!"
        return msg
myBall = Ball("red", "small", "down")
print(myBall)
