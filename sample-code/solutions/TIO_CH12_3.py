# TIO_CH12_3.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

# Answer to Try It Out Question 3 in Chapter 12

nameList = []
print("Enter 5 names (press the Enter key after each name):")
for i in range(5):
    name = input()
    nameList.append(name)

print("The third name is:", nameList[2])

