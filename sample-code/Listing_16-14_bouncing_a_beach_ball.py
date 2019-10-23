# Listing_16-14_bouncing_a_beach_ball.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load('beach_ball.png')
x = 50
y = 50
x_speed = 10  # Here’s the speed variable

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(20)
    # Put the ball-display code here, inside the `while` loop
    pygame.draw.rect(screen, [255,255,255], [x, y, 90, 90], 0)
    x = x + x_speed
    if x > screen.get_width() - 90  or  x < 0:  # When ball hits either edge of the window …
        x_speed = - x_speed  # … reverse direction by making speed the opposite sign.
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
pygame.quit()
