# Listing_25-1_building_the_skier_gameskier_only.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import pygame, sys, random

# Different images for the skier depending on his direction
skier_images = ["skier_down.png",
                  "skier_right1.png", "skier_right2.png",
                 "skier_left2.png", "skier_left1.png"]

class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0

    def turn(self, direction):
        self.angle = self.angle + direction
        # Don’t let the skier turn more than +/-2
        if self.angle < -2:  self.angle = -2
        if self.angle >  2:  self.angle =  2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6 - abs(self.angle) * 2]
        return speed

    # Move the skier left and right
    def move(self, speed):
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20:  self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620

# Redraw the screen
def animate():
    screen.fill([255, 255, 255])
    screen.blit(skier.image, skier.rect)
    pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()
skier = SkierClass()
speed = [0, 6]

# Main Pygame event loop
running  = True
while running:
    clock.tick(30)
    for event in pygame.event.get():  # Check for keypresses
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            # Left arrow turns left
            if event.key == pygame.K_LEFT:
                speed = skier.turn(-1)
            # Right arrow turns right
            elif event.key == pygame.K_RIGHT:
                speed = skier.turn(1)
    skier.move(speed)
    animate()

pygame.quit()
