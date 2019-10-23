# Listing_13-4_creating_and_using_a_function_that_returns_a_value.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

# Function calculates tax and returns total
def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    return total  # Sends result back to the main program

my_price = float(input("Enter a price: "))

totalPrice = calculateTax(my_price, 0.06)  # Calls function and stores the result in `totalPrice`
print("price = ", my_price, " Total price = ", totalPrice)
