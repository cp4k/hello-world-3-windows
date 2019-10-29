# Listing_26-4_chat_server.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import select, socket

# Start the server and listen for connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 12345))
server_socket.listen()
server_socket.setblocking(False)  # Set our sockets to nonblocking mode

client_sockets = []
client_objects = {}

class Client:
    def __init__(self, socket):
        self.socket = socket
        self.text_typed = b""
        self.username = None

        socket.setblocking(False)
        msg = b'Welcome to the chat server!\r\n'
        msg += b'Please enter a username:\r\n'
        socket.send(msg)

    # We'll call this when there's more data to read or the client has closed the connection
    def receive_data(self):
        data = self.socket.recv(2048)  # Read up to 2,048 bytes at a time
        # When there's no more data to read, that means the client closed the connection
        if not data:
            self.close_connection()
            return
        for char in data:
            char = bytes([char])
            # When the user presses Enter, send the message that they've typed
            if char == b'\n':
                self.handle_command(self.text_typed.strip())
                self.text_typed = b""
            else:
                self.text_typed += char

    def handle_command(self, command):
        global client_objects
        if self.username == None:
            self.username = command
            msg = b'Hi, ' + self.username + b'!'
            msg += b' Type a message and press Enter to send it.\r\n'
            self.socket.send(msg)
        elif command == b'/quit':
            self.close_connection()
        else:
            msg = b'[' + self.username + b']: ' + command + b'\r\n'
            # Send the message to everyone else on the server
            for client_object in client_objects.values():
                if client_object == self or client_object.username == None:
                    continue
                client_object.socket.send(msg)

    def close_connection(self):
        global client_sockets, client_objects
        client_sockets.remove(self.socket)
        del client_objects[self.socket.fileno()]
        self.socket.close()

while True:
    ready_to_read = select.select([server_socket] + client_sockets, [], [])[0]  # Wait for something to happen with one of our sockets
    for sock in ready_to_read:
        if sock == server_socket:
            # Runs when the server gets a *new* connection
            new_connection, address = sock.accept()
            client_sockets.append(new_connection)
            client_objects[new_connection.fileno()] = Client(new_connection)
            server_socket.listen()  # Continue to listen for more connections
        # Runs when an *existing* client has sent something or closed the connection
        else:
            client_objects[sock.fileno()].receive_data()
