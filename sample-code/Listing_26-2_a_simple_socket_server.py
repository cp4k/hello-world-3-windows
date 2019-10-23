# Listing_26-2_a_simple_socket_server.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket for the server to use
s.bind(('', 12345))  # Bind the socket to port 12345

s.listen(1)  # Start listening for connections
connection, from_address = s.accept()  # Wait for someone to connect

connection.sendall(b"Hi there--oops, sorry, gotta go!\r\n")  # Respond to the connection with a message

# Close the connection
connection.shutdown(socket.SHUT_WR)
connection.close()
s.close()  # Close the server's socket
