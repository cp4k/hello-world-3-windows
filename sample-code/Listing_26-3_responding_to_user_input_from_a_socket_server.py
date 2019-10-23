# Listing_26-3_responding_to_user_input_from_a_socket_server.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import socket

# Start the server and accept a connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 12345))
s.listen(1)
connection, from_address = s.accept()

connection.sendall(b"Hi there! Welcome to my server!\r\nWhat's your name? ")

# Read data from the client one byte at a time
name = bytes()
while True:
    next_character = connection.recv(1)  # Wait for the client to send us a byte of data
    # Stop reading when Enter is pressed or no more data is available
    if next_character in [b'', b'\r', b'\n']:
        break
    else:
        name += next_character

connection.sendall(b"Nice to meet you, " + name + b"! Goodbye for now!\r\n")

connection.shutdown(socket.SHUT_WR)
connection.close()
s.close()
