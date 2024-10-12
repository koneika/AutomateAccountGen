import win32com.client

# start_vmbox(vm_name, 1) - gui
# start_vmbox(vm_name, ...) - heandless
def start_vmbox(vm_name, state):
    # Подключаемся к VirtualBox
    vbox = win32com.client.Dispatch("VirtualBox.VirtualBox")
    session = win32com.client.Dispatch("VirtualBox.Session")

    machine = vbox.FindMachine(vm_name)

    if state == 1:
        # Подключаемся к машине
        progress = machine.LaunchVMProcess(session, "gui", None)
    elif state == 0:
        progress = machine.LaunchVMProcess(session, "headless", None)

    # Ожидаем завершения запуска
    progress.WaitForCompletion(-1)

    # Закрываем сессию после завершения
    session.UnlockMachine()

# try to open a virtual box
try:
    start_vmbox("slava3", 0)
except:
    print("\"Yor virtual box is alredy work, continue write\"")



# create the data.txt file with answear
import os
import time

answear = None
logical_issue = 0

# really correct file direction
def CorrectFileDir(name_of_file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    new_file_name = name_of_file
    return os.path.join(current_dir, new_file_name)

# if you close your program in the half a progress
try: 
    with open(CorrectFileDir("dataOutput.txt"), 'r+', encoding='utf-8') as file2:
        answear = file2.read()
except:
    pass

# main
while True:
    print("Answear:", answear)
    answear = None
    hell_python = 0

    answear = str(answear)
    word = str(input())

    with open(CorrectFileDir("data.txt"), 'w') as file:
        file.write(word)

    # while open(CorrectFileDir("dataOutput.txt"), 'r+', encoding='utf-8'):
    #     with open(CorrectFileDir("dataOutput.txt"), 'r+', encoding='utf-8') as file2:
    #         answear = file2.read()
    #input("stop")

    while hell_python != 1:
        time.sleep(1)
        try: 
            if open(CorrectFileDir("dataOutput.txt"), 'r+', encoding='utf-8') and logical_issue == 0:
                print("1")
                os.remove(CorrectFileDir("dataOutput.txt"))
                logical_issue = 1

                while logical_issue == 1:
                    time.sleep(1)   
                    try:
                        if open(CorrectFileDir("dataOutput.txt"), 'r+', encoding='utf-8') and logical_issue == 1:

                            print("2")
                            with open(CorrectFileDir("dataOutput.txt"), 'r+', encoding='utf-8') as file2:
                                answear = file2.read()

                            os.remove(CorrectFileDir("dataOutput.txt"))
                            logical_issue = 0
                            hell_python = 1
                    except:
                        pass
                
                        
        except:
            pass





    
        
    # for i in range(2):
    #     while (open(CorrectFileDir("dataOutput.txt"), 'r+', encoding='utf-8')):
    #         time.sleep(1)  
    #         os.remove(CorrectFileDir("dataOutput.txt"))

    #             with open(CorrectFileDir("dataOutput.txt"), 'r+', encoding='utf-8') as file2:
    #                 answear = file2.read()
    #             os.remove(CorrectFileDir("dataOutput.txt"))

    



