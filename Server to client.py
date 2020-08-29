#!/usr/bin/python

"""Christopher T.  Server Program
    Copyright (C) 2020 Christopher T

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You can contact the author and get a copy of the orginial code from:
    https://github.com/xftransformers

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import socket

skt = socket.socket()
host = socket.gethostname()
port = 12345
skt.bind((host, port))

# ipaddresses = {'192.168.1.29':'Chris', '192.168.1.184':'James'}

# ipaddresses = {}
# ipadddreses["James"] = 192.168.1.184
# ipadddreses["Chris"] = 192.168.1.29
# ipadddreses[usernamefromClient] = addr


ipaddresses = {}
ipaddresses["192.168.1.184"] = "James"
ipaddresses["192.168.1.29"] = "Chris"

response="Hello"

# addr = '192.168.1.159'
# username_from_client = "James Laptop"
# ipaddresses[addr] = username_from_client


skt.listen(5)
while True:
    cli, addr = skt.accept()

    # username = ipaddresses[addr[0]]

    printName = addr[0]  # added this as Jon suggested

    # sends a message back to the client
    usernamefromClient = cli.recv(1024).decode(encoding='UTF-8')
    message_string = "Thank you for connecting, your username is " + usernamefromClient
    ipaddresses[addr[0]] = usernamefromClient

    message_bytes = message_string.encode(encoding='UTF-8')
    cli.send(message_bytes)
    response_bytes=response.encode(encoding='UTF-8')

    # prints the name that is already in the dictionary, as well as printing the clients desired name.
    # print(username, "has connected.")
    print("The user wants to use", usernamefromClient, "as a name.")

    # prints message from client.
    messageFromClient_string = cli.recv(1024).decode(encoding='UTF-8')

    if messageFromClient_string== "Hello":
        print(response, usernamefromClient)
        cli.send(response_bytes)
    else:
       print("This is a message from", usernamefromClient, messageFromClient_string)

    rightkeypressedclient = cli.recv(1024).decode(encoding='UTF-8')
    leftkeypressedclient = cli.recv(1024).decode(encoding='UTF-8')
    uparrowpressedclient = cli.recv(1024).decode(encoding='UTF-8')
    downarrowpressedclient = cli.recv(1024).decode(encoding='UTF-8')
    print(ipaddresses)
    print(rightkeypressedclient)
    print (leftkeypressedclient)
    print (uparrowpressedclient)
    print (downarrowpressedclient)

    cli.close()