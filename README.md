# Kivy-wireless-linux-keyboard-and-server
tablet or android keyboard for linux pc's

prerecquisites for client                                                                                                       

Download QPython from Google Play
Add the Numpy library(through the QPypi tool or pip console)

Transfer:

main.py,

android.txt,

keyboard.kv,

to the QPython Projects Folder, I use the QPython FTP service to do this.

On the Host PC

prerecquisites numpy, uinput

sudo pip install python-numpy

sudo pip install python-uinput

Launch uinput

sudo modprobe uinput, you can check the /dev directory after there should be a listing for uinput

launch server

sudo ./keys_server.py

