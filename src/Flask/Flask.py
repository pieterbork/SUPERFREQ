from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__)

#Create a User home page and check our app flask is operational
@app.route('/')
def index():
    return render_template('index.html')

#Error handling function
@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def errorpage(e):
    return("something going wrong here")

    #Run main program
if __name__ == '__main__':
    app.debug = True
    try:
        app.run(host='127.0.0.1', port=7721)
    except:
        print("Host on 127.0.0.1, Port: 7721, is currently unavailable.")