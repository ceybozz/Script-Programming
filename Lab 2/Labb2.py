import csv, requests, json  #Modules

def myMain():   # Main metod
    choose = 0
    while choose != 6:  # While not equal to
        choose = myMeny()
        if choose == 1: # Button 1 
            scanMyCsv()
        if choose == 2: # Button 2 
            csvToJson(myCsvPath, myJsonPath)
            showJson()
        if choose == 3: # Button 3
            addToMyCsv()
        if choose == 4: # Button 4
            del_person()
        if choose == 5: # Button 6
            print('Progam has now terminated. \nThank you for using it.')
            break   # Exit

def myMeny():   # Meny
    print('\n*******************************************************')
    print('--------------- Welcome to the CSV-Meny ---------------')
    print('*******************************************************\n')
    print('1. Scan original-file.')
    print('2. Show json-data.')
    print('3. Add person.')
    print('4. Delete person.')
    print('5. Exit.')
    print('\n*******************************************************\n')

    choose = int(input('Please choose a number between 1 - 6: '))   # Enter number (int)
    while choose < 1 or choose > 6: # While number over 
        choose = int(input('Number must be between 1 - 6. \nPlease try again: '))
    return choose   # Back to "choose"

def csvToJson(myCsvPath, myJsonPath):   #Converting csv to json
    jsonList = []   # Create a list

    with open(myCsvPath, encoding = 'utf-8-sig') as csvOpen:    # Open csv-file as (csvOpen)
        csvReader = csv.DictReader(csvOpen, delimiter = ';')    # Variable for reader

        for row in csvReader:   # Every row in the readed file
            jsonList.append(row)    # List adding row

    with open(myJsonPath, 'w', encoding = 'utf-8-sig') as jsonOpen: # Open json-file as (jsonOpen)
        jsonObj = json.dumps(jsonList, ensure_ascii = False, indent = 4)    # Variable for object
        jsonOpen.write(jsonObj) # Write (jsonObj) in (jsonOpen)

def scanMyCsv():    # Button 1, Scaning csv
    try:
        with open(myCsvPath, newline = '', encoding = 'utf-8-sig') as csvOpen:
            reader = csv.reader(csvOpen)
            for row in reader:
                print(row)
    except FileExistsError as error:    # Error
        print(error)

def showJson(): # Button 2, Show json
    with open(myJsonPath, 'r', encoding = 'utf-8-sig') as jsonOpen:
        jsonObj = json.load(jsonOpen)   # Variable for load
    print(json.dumps(jsonObj, indent = 4))

def addToMyCsv():   # Button 3, Add person

    # Varable for inputs
    userName = input('Type in username please: ')
    firstName = input('Type in firstname please: ')
    lastName = input('Type in lastname please: ')
    eMail = input('Type in e-mail please: ')

    list = [userName, firstName, lastName, eMail]
    with open(myCsvPath, 'a+', newline = '', encoding = 'utf-8-sig') as csvOpen:
        writer = csv.writer(csvOpen, delimiter = ';')   # Variable for writer
        writer.writerow(list)   # Write in list 
        csvOpen.close()

def del_person():   # Knapp 4, Ta bort person
    with open(myCsvPath, 'r', encoding='utf-8-sig') as readData:
        reader = csv.reader(readData, delimiter=';')
        arry = []
        delete = input('\nWho do you want to delete? \nUsername please: ')
        found = 0

        for row in reader:
            if row[0] == delete:
                found = 1
            else:
                arry.append(row)

        readData.close()

        if found == 0:
            print('Sorry did not found ' + delete + '...')
        else:
            with open(myCsvPath, 'w+', newline='', encoding='utf-8-sig') as writeData:
                writer = csv.writer(writeData, delimiter=';')
                writer.writerows(arry)
                print('\n--> ' + delete + ' <-- is now deletet.')
                writeData.close()

def saveMyCsv():    #Save file
    with open(myCsvPath, 'a', encoding = 'utf-8-sig') as csvOpen:
        writer = csv.writer(csvOpen, delimiter = ";")
        print('File is saved!')
        csvOpen.close()

myCsvPath = './data/labb2-personer.csv' # Csv path
myJsonPath = './data/json-labb2-personer.json'  # Json path

myMain()    # Run my main method 