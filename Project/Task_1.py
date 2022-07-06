import imp
import json
from flask import Flask
from sympy import python
from subprocess import call

app = Flask(__name__)

rev = call('python reverse.py', shell=True)
cea = call('python ceasar.py', shell=True)
rov = call('python rovarsprak.py', shell=True)

@app.route('/reverse')
def reverse():
    with open("Rev.txt", "r+") as newFile:
        info=newFile.read()
    return info

@app.route('/ceasar')
def ceasar():
    with open("Cea.txt", "r+") as newFile:
        info=newFile.read()
    return info

@app.route('/rovarsprak')
def rovarsprak():
    with open("Rov.txt", "r+") as newFile:
        info=newFile.read()
    return info

app.run()