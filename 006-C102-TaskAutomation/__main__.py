# TaskAutomation
# This is a python script made by @somePythonProgrammer 
# for a WhiteHat Junior project.

# imports
import os
import shutil
import tqdm
from datetime import datetime
import time

# This function lists all directories 
# and subdirectories in a list.
def list_dirs(path):
    dirs_ = []
    for dirpath,_,filenames in os.walk(path):
        for f in filenames:
            dirs_.append(os.path.abspath(os.path.join(dirpath, f)))
    return dirs_

# This function dates the creation date of a file.
def date_file(file):
    created = os.path.getctime(file)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    return "%02d/%02d/%d"%(day,month,year)

# This function creates folders with a name.
def create_folder(path, name):
    try:
        os.mkdir(path +'/'+ name)
    except FileExistsError:
        pass

# This function moves a file to a new directory.
def move_file(file, path):
    shutil.move(file, path)

# The main function.
def main():
    # This is the path to the folder where the files are.
    d = input('Enter the path to the directory: ')
    # This creates a list of all files in the directory.
    dirs = list_dirs(d)
    # list of dates already created.
    dates_named = []
    # Loop through the files with progrss bars for very lasy people.
    for dir in tqdm.tqdm(dirs, desc='Progress'):
        # Get the creation date of the file.
        date = date_file(dir)
        # If the date is not in the list of dates already created.
        if not date in dates_named:
            # Get what the name of the folder should be.
            event = input(f"\nWhat happened on {' '+date} (e.g. Trip, NASA Tour, etc.): ")
            # Create a folder with the date.
            create_folder(d, event)
            # Move the file to the new folder and save the date to the list.
            dates_named.append(date)
            move_file(dirs[dirs.index(dir)], d + '/' + event)
        else:
            pass

# run the main function
if __name__ == '__main__':
    main()
