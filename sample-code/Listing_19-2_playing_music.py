# Listing_19-2_playing_music.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import pygame, sys
pygame.init()

screen = pygame.display.set_mode([640,480])

# These are the two changed lines.
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
