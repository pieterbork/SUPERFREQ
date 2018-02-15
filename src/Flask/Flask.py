#!/usr/bin/env python2

#author : Jing Guo jing.guo@colorado.edu
#name : Flask.py
#purpose :  The friendly GUI for novice users
#date : 2018.02.14
#version : 1.0.1
#version notes (latest): Compatible w/ python2. 


from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import thread
import webbrowser

app = Flask(__name__)

#Create thread for our webpage
def homePageThread():
    #Web Browser url will change...leave for testing
    webbrowser.open_new_tab('http://127.0.0.1:7721')

#Create a User home page and check our app flask is operational
@app.route('/')
def index():
    return render_template('index.html')

#Error handling function
@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def errorpage(e):
    return("Move along...nothing to see here :)")

#Run main program
if __name__ == '__main__':
    #Turn debugging off when code is ready for production :)
    app.debug = True
    try:
        #Test Environment code
        #thread.start_new_thread(homePageThread, ())
        app.run(host='127.0.0.1', port=7721)
        #Production environment code
        '''
        thread.start_new_thread(homePageThread, ())
        app.run(host='127.0.0.1', port=7721, reloader=False)
        '''
    except:
        print("Host on 127.0.0.1, Port: 7721, is currently unavailable.")
