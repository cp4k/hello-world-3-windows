# Listing_26-7_networked_chat_client.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import pygame
import socket  # Add this import

pygame.init()

screen_width, screen_height = screen_size = (640, 640)  # Make the screen taller to fit more messages
font = pygame.font.Font(None, 50)
bg_color = (0, 0, 0)
text_color = (255, 255, 255)
space_character_width = 8
message_spacing = 8

# Connect to the server
connection = socket.create_connection(('localhost', 12345))
connection.setblocking(False)
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
        word_surf = font.render(word, True, text_color, bg_color)
        if word_x + word_surf.get_width() > screen_width:
            word_x = 0
            word_y = text_height
        word_surfs.append(word_surf)
        word_locations.append((word_x, word_y))
        word_x += word_surf.get_width() + space_character_width
        if word_y + word_surf.get_height() > text_height:
            text_height = word_y + word_surf.get_height()

    surf = pygame.Surface((screen_width, text_height))
    surf.fill(bg_color)
    for i in range(len(words)):
        surf.blit(word_surfs[i], word_locations[i])
    return surf

# New code to keep track of past messages
message_surfs = []

def add_message(message):
    if len(message_surfs) > 50:
        message_surfs.pop(0)
    message_surfs.append(message_to_surface(message))

# New code to read from the socket
text_from_socket = b''
def read_from_socket():
    global connection, text_from_socket, running
    try:
        data = connection.recv(2048)
    # Handle the error caused by non-blocking mode
    except BlockingIOError:
        return

    # Stop the program when the connection closes
    if not data:
        running = False
    for char in data:
        char = bytes([char])
        if char == b'\n':
            add_message(text_from_socket.strip().decode('utf-8'))  # Convert the message from the server from `bytes` to a string, and draw it
            text_from_socket = b''
        else:
            text_from_socket += char

# New function to draw all the messages on the screen
def redraw_screen():
    screen.fill(bg_color)

    typing_surf = message_to_surface("> " + typing_text)
    y = screen_height - typing_surf.get_height()
    screen.blit(typing_surf, (0, y))

    message_index = len(message_surfs) - 1
    while y > 0 and message_index >= 0:
        message_surf = message_surfs[message_index]
        message_index -= 1
        y -= message_surf.get_height() + message_spacing
        screen.blit(message_surf, (0, y))
    pygame.display.flip()

running = True
typing_text = ""
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
                # New code to send a message to the server
                add_message('You: ' + typing_text)
                connection.send(typing_text.encode('utf-8') + b"\r\n")
                typing_text = ""
            else:
                typing_text += event.unicode

    # Update the main loop to call our new functions
    read_from_socket()
    redraw_screen()

pygame.quit()
connection.close()  # Close the connection when we're done
