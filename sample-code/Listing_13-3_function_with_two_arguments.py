# Listing_13-3_function_with_two_arguments.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

def printMyAddress(someName, houseNum):  # Uses two variables for two arguments
    # Both variables get printed
    print(someName)
    print(houseNum, "Main Street")
    print("Ottawa, Ontario, Canada")
    print("K2M 2E9")
    print()

# Calls the function, passing it two parameters
printMyAddress("Carter Sande", "45")
printMyAddress("Jack Black", "64")
printMyAddress("Tom Green", "22")
printMyAddress("Todd White", "36")
