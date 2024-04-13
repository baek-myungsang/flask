from flask import Flask
import random
 
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return 'random : <strong>' + str(random.random())  + '</strong>'
#  리턴값은 기본적으로 문자열
 
app.run(port=5001 ,debug=True)