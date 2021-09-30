# Folder Cleaner
# Made by somePythonProgrammer as a WhiteHat project.

import os
import time

dir_path = input('Enter folder path: ')

treshold = time.time() - 30*86400
for i in os.listdir(dir_path):
    try:
        if os.path.getmtime(dir_path + '\\' + i) < treshold:
            os.remove(dir_path + '\\' + i)
            print(i + ' deleted.')
    except:
        pass
