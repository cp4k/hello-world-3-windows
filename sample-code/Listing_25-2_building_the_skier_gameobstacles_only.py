# Listing_25-2_building_the_skier_gameobstacles_only.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import pygame, sys, random

# Class for obstacle sprites (trees and flags)
class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, obs_type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.obs_type = obs_type
        self.passed = False

    def update(self):
        global speed
        self.rect.centery -= speed[1]

# Create one screen of obstacles: 640 x 640
def create_map():
    global obstacles
    locations = []
    for i in range(10):  # 10 obstacles per screen
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location  = [col * 64 + 32, row * 64 + 32 + 640]
        if not (location in locations):  # Prevent 2 obstacles in the same place
            locations.append(location)
            obs_type = random.choice(["tree", "flag"])
            if obs_type == "tree": img = "skier_tree.png"
            elif obs_type == "flag":  img = "skier_flag.png"
            obstacle = ObstacleClass(img, location, obs_type)
            obstacles.add(obstacle)

# Redraw everything
def animate():
    screen.fill([255, 255, 255])
    obstacles.draw(screen)
    pygame.display.flip()

# Initialize everything
pygame.init()
screen = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()
speed = [0, 6]
obstacles = pygame.sprite.Group()
map_position = 0
create_map()

# Main loop
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    map_position += speed[1]  # Keep track of how far the obstacles have scrolled up

    # Create a new block of obstacles at the bottom
    if map_position >= 640:
        create_map()
        map_position = 0

    obstacles.update()
    animate()

pygame.quit()
