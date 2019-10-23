# Listing_11-5_printing_the_loop_variables_in_nested_loops.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

numBlocks = int(input('How many blocks of stars do you want? '))
for block in range(1, numBlocks + 1):
    print('block =', block)  # Displays variables
    for line in range(1, block * 2 ):
        for star in range(1, (block + line) * 2):
            print('* ', end='')
        print('  line =', line, 'star =', star)
    print()
