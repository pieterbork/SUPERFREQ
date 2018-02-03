#!/usr/bin/env python3

#author : Kade Cooper kaco0964@colorado.edu
#name : main.py
#purpose :  Allow user to choose between terminal and web browser environments
#date : 2018.02.02
#version : 1.0.3
#version notes (latest): Optimized for python3. Separate coding effort for future efforts


from tkinter import *
import subprocess
#Call the terminal.py file directly
#import terminal

#Create window
root=Tk()

########################## Functions ##########################

#Function to close the window
def closeWindow():
    root.destroy()

#Run terminal process
def runTerminal():
    try:
        #terminal.runTerminalMain()
        #Spawn a new terminal process just in case a user wishes to have a terminal and a web browser open
        subprocess.call("x-terminal-emulator -e bash -c './terminal.py' \"$1\"", shell=True)
        display.configure(text='Success Running Terminal!')
    except:
        display.configure(text='Failure Running Terminal!')

#Run browser process
def runWebBrowser():
    try:
        #terminal.runTerminalMain()
        display.configure(text='Success Running Web Browser!')
    except:
        display.configure(text='Failure Running Web Browser!')

########################## GUI Setup ########################

#Grid 1 display
Label(root, text="Choose Work Environment Below:").grid(columnspan=3, sticky=N)
#Create empty grid
display = Label(root, width=40, height=10, text="Status Updates Here")
display.grid(sticky=W)

#Buttons...use lambda so all buttons do not immediately run once the window starts
buttonTerminal=Button(root, text="Terminal", command=lambda:runTerminal()).grid(column=1,row=1)
buttonBrowser=Button(root, text="Web Browser", command=lambda:runWebBrowser()).grid(column=2,row=1)
buttonDestroy=Button(root, text="Close Program", command=lambda:closeWindow()).grid(columnspan=3,sticky=N+S+E+W)

"""Window Logic"""
root.grid_columnconfigure(0,weight=1) #Dynamically resize the widget in the window
root.resizable(True,True) #(True,False) Stops vertical resizing

"""Keep window from self updating in size"""
root.update()
root.geometry(root.geometry())

#Name of Program
root.title('SUPERFREQ Environment Chooser')
root.mainloop()
