# Listing_26-5_typing_in_a_message.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import pygame

pygame.init()

screen_width, screen_height = screen_size = (640, 320)
font = pygame.font.Font(None, 50)
bg_color = (0, 0, 0)
text_color = (255, 255, 255)

screen = pygame.display.set_mode(screen_size)
pygame.key.set_repeat(300, 100)

typing_text = ""  # Start out with no text on the screen

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if typing_text:
                    typing_text = typing_text[:-1]  # Delete the last character of the displayed text
            elif event.key == pygame.K_RETURN:
                typing_text = ""
            else:
                typing_text += event.unicode  # Add the letter the user typed to the displayed text

    screen.fill(bg_color)
    # Draw the text on the bottom of the screen
    typing_surf = font.render(typing_text, True, text_color, bg_color)
    screen.blit(typing_surf, (0, screen_height - typing_surf.get_height()))
    pygame.display.flip()

pygame.quit()
