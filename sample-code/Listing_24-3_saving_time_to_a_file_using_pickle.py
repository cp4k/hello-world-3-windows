# Listing_24-3_saving_time_to_a_file_using_pickle.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

# Imports `datetime`, `pickle`, and `os` modules
import datetime, pickle
import os

first_time = True
if os.path.isfile("last_run.pkl"):  # Checks if the pickle file exists
    pickle_file = open("last_run.pkl", 'rb')  # Opens pickle file for reading (if it exists)
    last_time = pickle.load(pickle_file)  # Unpickles the `datetime` object
    pickle_file.close()
    print("The last time this program was run was ", last_time)
    first_time = False

pickle_file = open("last_run.pkl", 'wb')  # Opens (or creates) the pickle file for writing
pickle.dump(datetime.datetime.now(), pickle_file)  # Pickles the `datetime` object of the current time
pickle_file.close()
if first_time:
    print("Created new pickle file.")
