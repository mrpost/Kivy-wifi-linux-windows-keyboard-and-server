#!/usr/bin/python

import win32api
import socket
import numpy as np
import time
import win32con
import ctypes

HOST = ''; # sets host to 127.0.0.1 the reserved IP address of your network iFace
PORT = 43565; #This can be set to any number as long as host and client match


y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]


controls = [0x11, 0x12, 0x20, 0x10, 0x26, 0x28, 0x25, 0x27, 0x31, 0x32, 0xAE, 0xAF, 0xC0, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30, 0xBD, 0xBB, 0x08, 0x09, 0x51, 0x57, 0x45, 0x52, 0x54, 0x59, 0x55, 0x49, 0x4F, 050, 0xDB, 0xDD, 0xDC, 0x14, 0x41, 0x53, 0x44, 0x46, 0x47, 0x48, 0x4A, 0x4B, 0x4C, 0xBA, 0xDE, 0x0D, 0x5A, 0x58, 0x43, 0x56, 0x42, 0x4E, 0x4D, 0xBC, 0xBE, 0xBF, 0xAD, 0x1B, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7A, 0x7B, 0x2E, 0x24, 0x23, 0x21, 0x22]

DirectX = [0x1D, 0x38, 0x39, 0x2A, 0xC8, 0xD0, 0xCB, 0xCD, 0x02, 0x03, 0xAE, 0xAF, 0x29, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x2B, 0x3A, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x1C, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0xAD, 0x01, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40, 0x41, 0x42, 0x43, 0x44, 0x57, 0x58, 0xD3, 0xC7, 0xCF, 0xC9, 0xD1]
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
    
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):   
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

while True:
    d = sock.recvfrom(1024)
    data = d[0]
    data = np.fromstring(data, dtype=np.uint32)
    if data[1] == 1:
         win32api.keybd_event(controls[data[0]],0,0,0)
         #print controls[data[0]] 'this line I used for testing you can uncomment to insure server is recieving commands'
    elif data[1] == 0:
        win32api.keybd_event(controls[data[0]], 0, win32con.KEYEVENTF_KEYUP, 0)
    elif data[1] == 3:
        PressKey(DirectX[data[0]])
        #print DirectX[data[0]]
    elif data[1] == 4:
        #ReleaseKey(DirectX[data[0]])
        print DirectX[data[0]]
    #time.sleep(.05)        
