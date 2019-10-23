# Listing_13-7_trying_to_modify_a_global_variable_inside_a_function.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)

    # The variable `my_price` here is in a different chunk of memory than the `my_price` here.
    my_price = 10000  # Modifies `my_price` inside the function
    print("my_price (inside function) = ", my_price)  # Prints the local version of `my_price`
    return total

my_price = float(input("Enter a price: "))

totalPrice = calculateTax(my_price, 0.06)
print("price = ", my_price, " Total price = ", totalPrice)
print("my_price (outside function) = ", my_price)  # Prints the global version of `my_price`
