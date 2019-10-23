# Listing_19-1_trying_out_sounds_in_pygame.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import pygame, sys
pygame.init()  # Initializes Pygame

screen = pygame.display.set_mode([640,480])  # Creates a Pygame window

splat = pygame.mixer.Sound("splat.wav")  # Creates the `Sound` object
splat.play()  # Plays the sound

running = True
# The usual Pygame event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
