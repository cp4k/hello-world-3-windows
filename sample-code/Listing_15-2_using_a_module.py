# Listing_15-2_using_a_module.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import my_module  # `my_module` contains the `c_to_f()` function

celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = c_to_f(celsius)
print("That's", fahrenheit, "degrees Fahrenheit")
