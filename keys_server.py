#!/usr/bin/python

import uinput
import socket
import numpy as np
import time

HOST = ''; # sets host to 127.0.0.1 the reserved IP address of your network iFace
PORT = 43565; #This can be set to any number as long as host and client match


y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]

device = uinput.Device([uinput.KEY_LEFTCTRL, uinput.KEY_LEFTALT, uinput.KEY_SPACE, uinput.KEY_LEFTSHIFT, uinput.KEY_UP, uinput.KEY_DOWN, uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_1, uinput.KEY_2, uinput.KEY_VOLUMEDOWN, uinput.KEY_VOLUMEUP, uinput.KEY_GRAVE, uinput.KEY_3, uinput.KEY_4, uinput.KEY_5, uinput.KEY_6, uinput.KEY_7, uinput.KEY_8, uinput.KEY_9, uinput.KEY_0, uinput.KEY_MINUS, uinput.KEY_EQUAL, uinput.KEY_BACKSPACE, uinput.KEY_TAB, uinput.KEY_Q, uinput.KEY_W, uinput.KEY_E, uinput.KEY_R, uinput.KEY_T, uinput.KEY_Y, uinput.KEY_U, uinput.KEY_I, uinput.KEY_O, uinput.KEY_P, uinput.KEY_LEFTBRACE, uinput.KEY_RIGHTBRACE, uinput.KEY_BACKSLASH, uinput.KEY_CAPSLOCK, uinput.KEY_A, uinput.KEY_S, uinput.KEY_D, uinput.KEY_F, uinput.KEY_G, uinput.KEY_H, uinput.KEY_J, uinput.KEY_K, uinput.KEY_L, uinput.KEY_SEMICOLON, uinput.KEY_APOSTROPHE, uinput.KEY_ENTER, uinput.KEY_Z, uinput.KEY_X, uinput.KEY_C, uinput.KEY_V, uinput.KEY_B, uinput.KEY_N, uinput.KEY_M, uinput.KEY_COMMA, uinput.KEY_DOT, uinput.KEY_SLASH, uinput.KEY_MUTE, uinput.KEY_ESC, uinput.KEY_F1, uinput.KEY_F2, uinput.KEY_F3, uinput.KEY_F4, uinput.KEY_F5, uinput.KEY_F6, uinput.KEY_F7, uinput.KEY_F8, uinput.KEY_F9, uinput.KEY_F10, uinput.KEY_F11, uinput.KEY_F12, uinput.KEY_DELETE, uinput.KEY_HOME, uinput.KEY_END, uinput.KEY_PAGEUP, uinput.KEY_PAGEDOWN])

controls = [uinput.KEY_LEFTCTRL, uinput.KEY_LEFTALT, uinput.KEY_SPACE, uinput.KEY_LEFTSHIFT, uinput.KEY_UP, uinput.KEY_DOWN, uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_1, uinput.KEY_2, uinput.KEY_VOLUMEDOWN, uinput.KEY_VOLUMEUP, uinput.KEY_GRAVE, uinput.KEY_3, uinput.KEY_4, uinput.KEY_5, uinput.KEY_6, uinput.KEY_7, uinput.KEY_8, uinput.KEY_9, uinput.KEY_0, uinput.KEY_MINUS, uinput.KEY_EQUAL, uinput.KEY_BACKSPACE, uinput.KEY_TAB, uinput.KEY_Q, uinput.KEY_W, uinput.KEY_E, uinput.KEY_R, uinput.KEY_T, uinput.KEY_Y, uinput.KEY_U, uinput.KEY_I, uinput.KEY_O, uinput.KEY_P, uinput.KEY_LEFTBRACE, uinput.KEY_RIGHTBRACE, uinput.KEY_BACKSLASH, uinput.KEY_CAPSLOCK, uinput.KEY_A, uinput.KEY_S, uinput.KEY_D, uinput.KEY_F, uinput.KEY_G, uinput.KEY_H, uinput.KEY_J, uinput.KEY_K, uinput.KEY_L, uinput.KEY_SEMICOLON, uinput.KEY_APOSTROPHE, uinput.KEY_ENTER, uinput.KEY_Z, uinput.KEY_X, uinput.KEY_C, uinput.KEY_V, uinput.KEY_B, uinput.KEY_N, uinput.KEY_M, uinput.KEY_COMMA, uinput.KEY_DOT, uinput.KEY_SLASH, uinput.KEY_MUTE, uinput.KEY_ESC, uinput.KEY_F1, uinput.KEY_F2, uinput.KEY_F3, uinput.KEY_F4, uinput.KEY_F5, uinput.KEY_F6, uinput.KEY_F7, uinput.KEY_F8, uinput.KEY_F9, uinput.KEY_F10, uinput.KEY_F11, uinput.KEY_F12, uinput.KEY_DELETE, uinput.KEY_HOME, uinput.KEY_END, uinput.KEY_PAGEUP, uinput.KEY_PAGEDOWN]

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    print "Socket Created"
except socket.error, msg:
    print "socket failed. error code :" + str(msg[0]) + " Message " + msg[1]
    sys.exit()

try:
    sock.bind((HOST, PORT))
except socket.error, msg:
    print "socket failed. error code :" + str(msg[0]) + " Message " + msg[1]
    sys.exit()

while True:
    d = sock.recvfrom(1024)
    data = d[0]
    data = np.fromstring(data, dtype=np.uint32)
    if data[1] == 1:
         device.emit(controls[data[0]], 1)
         #print controls[data[0]] 'this line I used for testing you can uncomment to insure server is recieving commands'
    elif data[1] == 0:
        device.emit(controls[data[0]], 0)
    time.sleep(.05)        
