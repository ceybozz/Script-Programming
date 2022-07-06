from sqlite3.dbapi2 import paramstyle
from flask import Flask, redirect,escape, json, request, jsonify, render_template
from flask.helpers import url_for
from flask_cors import CORS
import bcrypt 
import sqlite3

app = Flask(__name__)   # Anger att detta är en flask app
app.config['SEND_FILE_MAX_DEFAULT'] = 0 # Subclass, can be modified like dictionary

@app.route('/', methods=['POST', 'GET'])    # Skapar en main hemsida med hjälp av post och get metoderna
def signup():
    if request.method == 'POST':    
        paymenttype = request.form['paymenttype'] # Variabel för alla 12 värden, (Hämtar värdet från fälten och sätter det på en variabel)
        fistname = request.form['fname'] 
        aftername = request.form['ename'] 
        adress = request.form['address']  
        district = request.form['zipcode']  
        city = request.form['city'] 
        phone = request.form['cellphone']
        email = request.form['email']   
        password = request.form['pwd']
        offers = request.form['offers']
        typeformat = request.form['format']
        textcomment = request.form['comment']
        return '''<h1>Registrerade uppgifter: </h1>
                  <li><b>Betalsätt:</b> {}</li>
                  <li><b>Förnamn:</b> {}</li>
                  <li><b>Efternamn:</b> {}</li>
                  <li><b>Adress:</b> {}</li>
                  <li><b>Postnummer:</b> {}</li>
                  <li><b>Ort:</b> {}</li>
                  <li><b>Mobil:</b> {}</li>
                  <li><b>E-post:</b> {}</li>
                  <li><b>Lösenord:</b> {}</li>
                  <li><b>Erbjudande:</b> {}</li>
                  <li><b>E-postformat:</b> {}</li>
                  <li><b>Kommerntar:</b> {}</li>'''.format(paymenttype, fistname, aftername, adress, district, city, phone, email, password, offers, typeformat, textcomment) # Returerar listan -- (Formaterar innehållet i måsvingarna med variablena som angetts och returnerar en html stylad lista med värdena)
    return render_template('index.html')    # Returerar till index.html

if __name__ == '__main__':  # Programmet körs direkt som en FLASK_APP istället för att behöva set använda set metoden i visual studio terminalen
    app.run()