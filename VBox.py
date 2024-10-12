import os
import time
# import win32api
# import win32con
import pyautogui

word = None

def CorrectFileDir(name_of_file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    new_file_name = name_of_file
    return os.path.join(current_dir, new_file_name)

# 1 - input
# 0 - output
def ioFile(switcher, filename):
    global word

    if switcher == "i":
        try:
            with open(CorrectFileDir(filename), 'w') as file:
                file.write(word)
            return word
        
        except FileNotFoundError:
            return None
    elif switcher == "o":
        try:
            with open(CorrectFileDir(filename), 'r+') as file:
                word = file.read()
            return word
        except FileNotFoundError:
            return None
        
while True:
    
    time.sleep(0.1)
    writeIt = ioFile("o", "data.txt")

    if writeIt != None:
        print(writeIt)
        pyautogui.write(writeIt)
        time.sleep(1)
        pyautogui.keyDown("enter")
        os.remove(CorrectFileDir("data.txt"))





















    # try:
    #     word = ioFile("o", "data.txt")
    #     if word:
    #         print(word)
    #         #converter(ioFile("o", "data.txt"))
    #         print(ord(word[0]))
    #         win32api.keybd_event(ord(ioFile("o", "data.txt")[0]), 0, 0, 0)  # Зажать клавишу 'A'
    #         win32api.keybd_event(ord(ioFile("o", "data.txt")[0]), 0, win32con.KEYEVENTF_KEYUP, 0)  # Отжать клавишу 'A'
        
        
    #     os.remove("data.txt")
    #     word = None
    #     ioFile("o", None)
    # except FileNotFoundError:
    #     pass

    
    