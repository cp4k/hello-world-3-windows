# Listing_16-13_moving_a_beach_ball_image_smoothly.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load('beach_ball.png')
# Add these lines
x = 50
y = 50
screen.blit(my_ball,[x, y])  # Uses `x` and `y` (instead of numbers)
pygame.display.flip()
for looper in range (1, 100):  # Starts a `for` loop
    pygame.time.delay(20)  # `time.delay` value changed from `2000` to `20`
    pygame.draw.rect(screen, [255,255,255], [x, y, 90, 90], 0)
    x = x + 5
    screen.blit(my_ball, [x, y])
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
