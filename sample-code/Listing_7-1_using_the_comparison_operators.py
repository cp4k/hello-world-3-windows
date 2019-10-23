# Listing_7-1_using_the_comparison_operators.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 < num2:
    print(num1, "is less than", num2)
if num1 > num2:
    print(num1, "is greater than", num2)
if num1 == num2:  # Remember that this is a double equal sign
    print(num1, "is equal to", num2)
if num1 != num2:
    print(num1, "is not equal to", num2)
