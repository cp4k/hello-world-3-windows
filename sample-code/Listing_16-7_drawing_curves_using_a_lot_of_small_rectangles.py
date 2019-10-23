# Listing_16-7_drawing_curves_using_a_lot_of_small_rectangles.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import pygame, sys
import math  # Imports the math functions, including `sin()`
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
for x in range(0, 640):  # Loops from left to right, _x_ = 0 to 639
    y = int(math.sin(x/640 * 4 * math.pi) * 200 + 240)  # Calculates the y-position (vertical) of each point
    pygame.draw.rect(screen, [0,0,0],[x, y, 1, 1], 1)  # Draws the point using a small rectangle
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
