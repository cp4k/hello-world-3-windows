# Listing_11-6_hot_dog_combinations.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

print("\tDog \tBun \tKetchup\tMustard\tOnions")
count = 1
for dog in [0, 1]:  # dog loop
    for bun in [0, 1]:  # bun loop
        for ketchup in [0, 1]:  # ketchup loop
            for mustard in [0, 1]:  # mustard loop
                for onion in [0, 1]:
                    print("#", count, "\t", end='')
                    print(dog, "\t", bun, "\t", ketchup, "\t", end='')
                    print(mustard, "\t", onion)  # onion loop
                    count = count + 1
