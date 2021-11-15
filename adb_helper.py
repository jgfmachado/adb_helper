'''
Created on Jan 22, 2021

@author: Guilherme
'''

from tkinter import Tk, Button, filedialog, simpledialog
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
    execute("adb connect 192.168.5.118:5555")
    
def adb_connect_androidtv():
    execute("adb disconnect")
    execute("adb connect 192.168.5.101:5555")

def adb_disconnect():
    execute("adb disconnect")
    
def take_screenshot():
    file_name = simpledialog.askstring("", "Input a name for the screenshot.\
    \nIt shouldn't be empty nor include forbidden characters.\
    \nForbidden characters:  <  >  :  \"  /  \\  |  ?  *")
    forbidden_chars = ['<','>',':','"','/','\\','|','?','*']
    if file_name != "" and file_name not in forbidden_chars:
        execute(f"adb exec-out screencap -p > {file_name}.png")

def display_device():
    execute_p("scrcpy -m 1920 -b 10M")
    
def install_pkg():
    my_filetypes = [('apk files', '.apk')]
    path = filedialog.askopenfilename(filetypes = my_filetypes)
    if path != "":
        execute_p(f'adb install "{path}"')
        

create_button("Connect to FireTV", 20, [10, 10], adb_connect_firetv)
create_button("Connect to AndroidTV", 20, [10, 50], adb_connect_androidtv)
create_button("Disconnect", 20, [10, 90], adb_disconnect)
create_button("Take screenshot", 20, [210, 10], take_screenshot)
create_button("Display device", 20, [210, 50], display_device)
create_button("Install .apk", 20, [210, 90], install_pkg)

root.resizable(False, False)
root.mainloop()