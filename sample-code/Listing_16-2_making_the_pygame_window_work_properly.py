# Listing_16-2_making_the_pygame_window_work_properly.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
running  = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
