'''
Created on Jan 22, 2021

@author: Guilherme
'''

from tkinter import Tk, Button, filedialog
from subprocess import run, Popen

root = Tk()
root.geometry("370x130")
root.title("ADB Helper")

def execute(command):
    run(command, shell=True)

def execute_p(command):
    Popen(command)

def create_button(text, width, position, command):
    button = Button(text = text, width = width, command = command)
    button.place(x = position[0], y = position[1])
    return button

def adb_connect_firetv():
    execute("adb disconnect")
    execute("adb connect 192.168.10.130:5555")
    

def adb_connect_androidtv():
    execute("adb disconnect")
    execute("adb connect 192.168.10.101:5555")
    
def display_device():
    execute_p("scrcpy -m 1600")
    
def install_pkg():
    my_filetypes = [('apk files', '.apk')]
    path = filedialog.askopenfilename(filetypes = my_filetypes)
    if path != "":
        execute_p(f'adb install -r "{path}"')

def adb_disconnect():
    execute("adb disconnect")

create_button("Connect to FireTV", 20, [10, 30], adb_connect_firetv)
create_button("Connect to AndroidTV", 20, [10, 70], adb_connect_androidtv)
create_button("Display device", 20, [210, 10], display_device)
create_button("Install .apk", 20, [210, 50], install_pkg)
create_button("Disconnect", 20, [210, 90], adb_disconnect)

root.resizable(False, False)
root.mainloop()