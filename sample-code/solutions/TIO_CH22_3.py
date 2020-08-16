# TIO_CH22_3.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

# Answer to Try It Out, Question 3, Chapter 22

# Save some data to a pickle file

import pickle

name = input("Enter your name: ")
age = input("Enter your age: ")
color = input("Enter your favorite color: ")
food = input("Enter your favorite food: ")

my_list = [name, age, color, food]

pickle_file = open("my_pickle_file.pkl", 'wb')  # Open in Binary mode
pickle.dump(my_list, pickle_file)

pickle_file.close()
