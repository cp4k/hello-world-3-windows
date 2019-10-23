# Listing_13-5_trying_to_print_a_local_variable.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

# Defines a function to calculate tax and return the total
def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    return total

my_price = float(input("Enter a price: "))

totalPrice = calculateTax(my_price, 0.06)  # Calls the function and stores and prints the result
print("price = ", my_price, " Total price = ", totalPrice)
print(price)  # Tries to print `price`
