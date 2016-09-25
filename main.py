#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy
import sys
sys.path.append('/data/data/org.qpython.qpy/files/lib/python2.7/site-packages/numpy-1.9.2-py2.7.egg') #the path varies depending on the version of QPython
import numpy as np 
import socket
import kivy
kivy.require('1.0.6')
import select

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition 
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.core.window import Window

HOST = HOST-IP-HERE; # syntax is 'IP #' you need the quotes around the IP #
PORT = 43565;

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print "no socket"


def on_pause(self):
    return True
    
def on_resume(self):
    pass


class KeyboardScreen(Screen):
    def dataS(self, a, b):
        arrS = np.array([a, b], dtype=np.uint32) 
        dataS = arrS.tostring()
        s.sendto(dataS, (HOST, PORT))

    


class HomeScreen(Screen):
    pass 
    


    
Builder.load_file("keyboard.kv")

sm = ScreenManager()
sm.add_widget(HomeScreen(name ='home'))
sm.add_widget(KeyboardScreen(name='keyboard'))

class KeyboardApp(App):

    def on_pause(self):
        return True

    def build(self):
        return sm 

if __name__ == '__main__':
    KeyboardApp().run()
