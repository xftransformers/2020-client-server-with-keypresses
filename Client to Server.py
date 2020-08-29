#!/usr/bin/python           # This is client.py file

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

import socket               # Import socket module
import time
from pygame.locals import *
import pygame
screen_width = 800
screen_length = 600
screen= pygame.display.set_mode((screen_width, screen_length), 0, 32)
leftkeymessage = "Left key was pressed!"
rightkeymessage = "Right key was pressed!"
downkeymessage = "Down key was pressed!"
upkeymessage = "Down key was pressed!"

usernameToServer=input("Please input a username you wish to use while connected. ")
messageToServer=input("Please input a message. ")
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
s.send((usernameToServer).encode(encoding='UTF-8'))
s.send((messageToServer).encode(encoding='UTF-8'))
messagefromserver =s.recv(1024).decode(encoding='UTF-8')
responsefromserver=s.recv(1024).decode(encoding='UTF-8')
print(messagefromserver, responsefromserver)
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                print("Right key was pressed.")
                s.send((rightkeymessage).encode(encoding='UTF-8'))
            if event.key == K_LEFT:
                print("Left key was pressed.")
                s.send((leftkeymessage).encode(encoding='UTF-8'))
            if event.key == K_UP:
                print ("Up arrow was pressed.")
                s.send((upkeymessage).encode(encoding='UTF-8'))
            if event.key == K_DOWN:
                print("Down arrow was pressed")
                s.send((downkeymessage).encode(encoding='UTF-8'))
            if event.key == K_ESCAPE:
                s.close()
                pygame.exit()