#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : main.py
#purpose :  Allow user to choose between terminal and web browser environments
#date : 2018.02.21
#version : 1.1.09
#version notes (latest): Compatible w/ python2. Spawns separate shell process


from Tkinter import *
import subprocess
#Call the terminal.py file within our "app" subdirectory
#from src.infrastructure import terminal

#Create window
root=Tk()

#Attach Icon to Program
programIcon = PhotoImage(file="./src/icons/hackrf_48_icon.png")
root.tk.call('wm', 'iconphoto', root._w, programIcon)

########################## Functions ##########################

#Function to close the window
def closeWindow():
    root.destroy()

#Run terminal process
def runTerminal():
    try:
        #terminal.runTerminalMain()
        #Spawn a new terminal process just in case a user wishes to have a terminal and a web browser open
        subprocess.call("x-terminal-emulator -e bash -c 'src/infrastructure/terminal.py' \"$1\"", shell=True)
        display.configure(text='Success Running Terminal!')
    except:
        display.configure(text='Failure Running Terminal!')

#Run browser process
def runWebBrowser():
    try:
        #Spawn a new flask process just in case a user wishes to have a web browser and a terminal open
        subprocess.call("x-terminal-emulator -e bash -c 'src/Flask/Flask.py' \"$1\"", shell=True)
        display.configure(text='Success Running Web Browser!')
    except:
        display.configure(text='Failure Running Web Browser!')

########################## GUI Setup ########################



#Images for Buttons
terminalIcon = PhotoImage(file="./src/icons/superfreq_terminal_icon.png")
flaskIcon = PhotoImage(file="./src/icons/superfreq_flask_icon.png")
closeIcon = PhotoImage(file="./src/icons/aurora_folder_close_program32_icon.png")

#Grid 1 display
Label(root, text="Choose Work Environment Below:", font=("TkTextFont", 18)).grid(columnspan=3, sticky=N)
#Create empty grid
display = Label(root, width=40, height=07, text="Status Updates Here")
display.grid(sticky=W)



#Non Icon Filled Code Below
'''
#Buttons...use lambda so all buttons do not immediately run once the window starts
buttonTerminal=Button(root, text="Terminal", command=lambda:runTerminal()).grid(column=1,row=1)
buttonBrowser=Button(root, text="Web Browser", command=lambda:runWebBrowser()).grid(column=2,row=1)
'''

####
####Working on getting images next to text buttons within Tkinter
####
buttonTerminal=Button(root, compound=LEFT, image=terminalIcon, text="Terminal", command=lambda:runTerminal()).grid(column=1,row=1)
buttonBrowser=Button(root, compound=LEFT, image=flaskIcon, text="Web Browser", command=lambda:runWebBrowser()).grid(column=2,row=1)
buttonDestroy=Button(root, compound=LEFT, image=closeIcon, text="Close Program", command=lambda:closeWindow()).grid(columnspan=3,sticky=N+S+E+W)

"""Window Logic"""
root.grid_columnconfigure(0,weight=1) #Dynamically resize the widget in the window
root.resizable(True,True) #(True,False) Stops vertical resizing

"""Keep window from self updating in size"""
root.update()
root.geometry(root.geometry())

#Name of Program
root.title('SUPERFREQ Environment Chooser')
root.mainloop()
