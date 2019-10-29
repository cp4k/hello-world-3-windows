# Listing_26-6_typing_in_a_message_with_word_wrapping.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import pygame

pygame.init()

screen_width, screen_height = screen_size = (640, 320)
font = pygame.font.Font(None, 50)
bg_color = (0, 0, 0)
text_color = (255, 255, 255)
space_character_width = 8  # Notice that we added this constant

screen = pygame.display.set_mode(screen_size)
pygame.key.set_repeat(300, 100)

def message_to_surface(message):
    words = message.split(' ')

    word_surfs = []
    word_locations = []
    word_x = 0
    word_y = 0
    text_height = 0

    for word in words:
        word_surf = font.render(word, True, text_color, bg_color)  # Create a surface with just one word
        # If the word is too wide to fit on the current line, move to the next line
        if word_x + word_surf.get_width() > screen_width:
            word_x = 0
            word_y = text_height
        word_surfs.append(word_surf)
        word_locations.append((word_x, word_y))
        word_x += word_surf.get_width() + space_character_width  # Add a space between this word and the next one
        if word_y + word_surf.get_height() > text_height:
            text_height = word_y + word_surf.get_height()

    # Draw all of the word surfaces onto a single big surface
    surf = pygame.Surface((screen_width, text_height))
    surf.fill(bg_color)
    for i in range(len(words)):
        surf.blit(word_surfs[i], word_locations[i])
    return surf

typing_text = ""

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
                    typing_text = typing_text[:-1]
            elif event.key == pygame.K_RETURN:
                typing_text = ""
            else:
                typing_text += event.unicode

    screen.fill(bg_color)
    typing_surf = message_to_surface(typing_text)  # Change this line to call our new text drawing function
    screen.blit(typing_surf, (0, screen_height - typing_surf.get_height()))
    pygame.display.flip()

pygame.quit()
