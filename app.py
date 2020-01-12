#The Simple Flask Program 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
        return("Hey ! Welcome ")

@app.route('/how you doing')
def hello():
        return("Hello there mate ! I am doing good, How about you ? ")

if __name__ == "__main__" :

    app.run(host='0.0.0.0')


