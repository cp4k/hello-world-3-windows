# Listing_11-7_hot_dog_program_with_calorie_counter.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

# Lists calories for each part of the hot dog
dog_cal = 140
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40

print("\tDog \tBun \tKetchup\tMustard\tOnions\tCalories")  # Prints headings
count = 1
for dog in [0, 1]:  # `dog` is the outer loop
    # Nested loops
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    # Calculates calories in the inner loop
                    total_cal = (bun * bun_cal)+(dog * dog_cal) + \
                        (ketchup * ket_cal)+(mustard * mus_cal) + \
                             (onion * onion_cal)
                    print("#", count, "\t", end='')
                    print(dog, "\t", bun, "\t", ketchup, "\t", end='')
                    print(mustard, "\t", onion, end='')
                    print("\t", total_cal)
                    count = count + 1
