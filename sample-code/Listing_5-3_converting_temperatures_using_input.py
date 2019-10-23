# Listing_5-3_converting_temperatures_using_input.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

print("This program converts Fahrenheit to Celsius.")
fahrenheit = float(input("Type in a temperature in Fahrenheit: "))  # Use `float(input())` to get Fahrenheit temperature from user
celsius = (fahrenheit - 32) * 5.0 / 9
print("That is ", end='')
print(celsius, end='')
print(" degrees Celsius.")
