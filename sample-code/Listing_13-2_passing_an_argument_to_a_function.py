# Listing_13-2_passing_an_argument_to_a_function.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

def printMyAddress(myName):  # Creates `myName` argument for the function
    print(myName)  # Prints the name
    print("123 Main Street")
    print("Ottawa, Ontario, Canada")
    print("K2M 2E9")
    print()

printMyAddress("Carter Sande")  # Passes “Carter Sande” as the argument to the function; the variable `myName` inside the function will have the value “Carter Sande”.
