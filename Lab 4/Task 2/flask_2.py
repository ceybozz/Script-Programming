from flask import Flask, jsonify, render_template, escape, request
import sqlite3

app = Flask(__name__)   # Anger att detta är en flask app

@app.route('/') #Skapar en main hemsida
def main():
    return render_template('index.html')    # Returerar till index.html

@app.route('/weather', methods=['GET']) # Skapar weather sida som du kan använda "GET"
def weather():
    conn = sqlite3.connect('datab.db')  # Variabel för sql-metoden databas, (Koppling till databasen)
    c = conn.cursor()   # Variabel för cursor-metoden, (Pekar på databasen med metoed cursor())
    c.execute('SELECT * FROM weather')  # Execute-metoden slår in genom hämta data, (Exekverar sql satsen med cursor som pekar på databsen)
    weather = c.fetchall() # Variabel för fetchall-metoden, (Hämtar all data med fetchall() och dumpar det på en variabeln weather)
    conn.commit()   # Commit metoden slår in
    return render_template('weather.html', weather=weather) #Returnerar till weather.html med datat på weather variabeln

@app.route('/addWeather', methods=['POST']) # Skapar addWeather sida som du kan använda "POST" på i postman appen
def add_temperature():
    conn = sqlite3.connect('datab.db')
    c = conn.cursor()
    p = (request.json['City'], request.json['Temperature']) # Variabel för json data, (Hämtar json data från fälten city och temperature och lägger det på variabeln p)
    c.execute('INSERT INTO weather (City, Temperature) VALUES(?,?)', p) # Execute metoden slår in genom lägga till data, (Exekverar sql satsen med cursor och lägger in json värdena i databasen)
    conn.commit()
    print(request.json) # Printar de värdena man postat i city och temperature i konsolen
    return {'Status' : 'Succeeded!'}    # Returerar text i postman teminalen

if __name__ == '__main__':  # Programmet körs direkt som en FLASK_APP istället för att behöva set använda set metoden i visual studio terminalen
    app.run()   # Programmet körs