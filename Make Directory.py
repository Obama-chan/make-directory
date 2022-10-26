import tkinter
from tkinter import filedialog
import os
import sys

tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
directory = filedialog.askdirectory() # Folders will be made in this directory unless variable is changed by user

print('Make folders in this directory' + directory)
name = ' '

while name != 'stop': #As long as user input isn't stop script will run
    name = input('Please enter the Foldername?:') #User prompt for input
    path = os.path.join(directory,name) #Will merge directory and foldername to absolute path

    if name == 'change': #if user enters Change File Explorer opens to allow user to pick new directory to make folder in
        tkinter.Tk().withdraw()
        directory = filedialog.askdirectory()
        print('Changing Directory to ' + path + '/n')
    elif name == 'stop': #if user enters stop script insta dies
        exit()
    elif os.path.exists(path): #else if to catch the exception of the folder already existing
        print('Already exists\n')
    else: #Else that will create the new folder
        os.mkdir(path)
        print('Created ' + name + ' in ' + directory + '\n')
