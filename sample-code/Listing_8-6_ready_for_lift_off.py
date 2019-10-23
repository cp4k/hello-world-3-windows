# Listing_8-6_ready_for_lift_off.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import time
for i in range(10, 0, -1):  # Counts backward
    print(i)
    time.sleep(1)  # Waits one second
print("BLAST OFF!")
