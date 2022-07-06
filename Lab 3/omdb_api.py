
import requests, json   # Modules
from io import BytesIO

json_list = []  # Lista 1 
title_list = [] # Lista 2

class omdb_buttons():   # Class 1, Buttons
    def my_Main(self):   # Main
        choose = 0
        while choose != 3:
            choose = self.my_menu() # Calling menu

            if choose == 1: # Button 1 
                search_titel = input('\nPlease enter title: ')  # Searching for title
                self.omdb_titel_URL('http://www.omdbapi.com/?apikey=3d2b7e74&s=' + search_titel)    # Calling my url + title
                title_list.append(search_titel)
                search_id = input('\nPlease enter ID: ')
                self.omdb_id_URL('http://www.omdbapi.com/?apikey=3d2b7e74&i=' + search_id)  # Calling my url + ID

            if choose == 2: # Button 2
                print(title_list)
                self.omdb_history()

            if choose == 3: # Button 3
                print('Progam has now terminated. \nThank you for using it.')
                quit()  # Ending program
                
    def my_menu(self):   # Menu
        print('\n*******************************************************')
        print('--------------- Welcome to the menu ---------------')
        print('*******************************************************\n')
        print('1. Search for movie.')
        print('2. View recent searches.')
        print('3. Exit.')
        print('\n*******************************************************\n')
        choose = int(input('Please enter number: '))   # Enter number (int)
        while choose < 1 or choose > 3: # While under 1 & over 3
            choose = int(input('Number must be between 1 - 3. \nPlease try again: '))
        return choose   # Back to "choose"
        
    def omdb_titel_URL(self, url): # Button 1, Fetch data
        response = requests.get(url)    # Variable for my request of url
        data = response.json()  # Variable for respose json-file
        for r in data['Search']:    # For every row in json-file
            print('\nTitle:', r['Title'])   # Printing title from json
            print('ID:', r['imdbID'])   # Printing ID from json

    def omdb_id_URL(self, url): # Button 1 
        response = requests.get(url)
        data = response.json()
        json_list.append(data['Title']) # Adding line data title
        json_list.append(data['Year'])
        json_list.append(data['Genre'])
        json_list.append(data['imdbID'])
        json_list.append(data['Plot'])
        json_list.append('--------------------------------------------------------------------------------------')
        print('\nTitle:', data['Title'])    # Printing "Title:" and the title 
        print('Year:', data['Year'])
        print('Genre:', data['Genre'])
        print('ID:', data['imdbID'])
        print('Plot:', data['Plot'])

    def omdb_history(self): # Button 2
        continued = True
        while continued:
            print('\n1. View information about recently searched movies. \n2. View information about selected movie search.\n')
            pick = int(input('Please enter number: '))
            if pick == 1:
                print(json.dumps(json_list, indent = 4))    # Printing json data from the list as 4 rows
            if pick == 2:
                print(json.dumps(json_list, indent = 4))
                search_id = input('Please enter ID: ')
                self.omdb_id_URL('http://www.omdbapi.com/?apikey=3d2b7e74&i=' + search_id)
            break

class omdb_init(omdb_buttons):  # Class 2, inherting from class 1
    def __init__(self): 
        self.my_Main()
        self.my_menu()