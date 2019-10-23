# Listing_16-8_a_well_connected_sine_wave.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import pygame, sys
import math
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
plotPoints = []
for x in range(0, 640):
    y = int(math.sin(x/640 * 4 * math.pi) * 200 + 240)  # Calculates y-position for each point
    plotPoints.append([x, y])  # Adds each point to the list
pygame.draw.lines(screen, [0,0,0], False, plotPoints, 1)  # Draws the whole curve with the `draw.lines()` function
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
