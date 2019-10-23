# Listing_13-6_using_a_global_variable_inside_a_function.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    print(my_price)  # Tries to print `my_price`
    return total

my_price = float(input("Enter a price: "))

totalPrice = calculateTax(my_price, 0.06)
print("price = ", my_price, " Total price = ", totalPrice)
