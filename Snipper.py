import tkinter
import tkinter.filedialog
import tkinter.simpledialog
import time

import pyautogui
from pynput import keyboard

start_file_name = ""
start_num = 0
pic_initial_point = pyautogui.position()
running = True

def on_press(key):
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))
    pass


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

    global pic_initial_point, running, start_num

    try:

        if key.char == 'z':
            pic_initial_point = pyautogui.position()

        if key.char == 'x':
            pyautogui.screenshot(start_file_name + str(start_num) + ".png", region=(
                pic_initial_point.x, pic_initial_point.y, abs(pyautogui.position().x - pic_initial_point.x),
                abs(pyautogui.position().y - pic_initial_point.y)))
            start_num += 1

        if key.char == '`':
            running = False

    except AttributeError:
        pass


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)


def main():
    global start_file_name, start_num

    listener.start()

    root = tkinter.Tk()
    root.withdraw()
    dir_name = tkinter.filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')

    start_file_name = tkinter.filedialog.asksaveasfilename(parent=root, initialdir=dir_name)

    print(start_file_name)

    start_num = tkinter.simpledialog.askinteger("File Number", "What file number would you like to start at?")

    while(running):
        time.sleep(1);


main();
