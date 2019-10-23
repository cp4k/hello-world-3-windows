# Listing_11-4_a_trickier_version_of_blocks_of_stars.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

numBlocks = int(input('How many blocks of stars do you want? '))
for block in range(1, numBlocks + 1):
    # Formulas for number of lines and stars
    for line in range(1, block * 2):
        for star in range(1, (block + line) * 2):
            print('* ', end='')
        print()
    print()
