from random import randint
import random
max_guess = 10  #Variabel för maximala gissningar
ok_guess = 7    #Variabel för godkänt gissningarer

def rnge(): #Funktion ett
    rnge = random.sample(range(1, 1000), 15)    #Random val mellan 1 till 1000, väljer 12 val.
    print(rnge) #Visar listan på alla 12 val
    for i in rnge:  #För varje tal i listan
        if i % 4 == 0 or i % 9 == 0:   #Om varje tal är delbart med 7 eller 11
            print(i)    #Visa talen

def guess():    #Funktion två            
        global ok_guess #Indicerar att vi använder globala ok_guess
        ok_guess = 0
        nr_list = []    #Skapar en tom lista
        name = input('Name:\n')    #Variabel för namn
        nr = randint(1, 100)    #Randomiserar ett tal mellan 1 till 100
        while ok_guess < max_guess: #While loop 
            guess = int(input("Guess number:\n"))    #Variabel för chansing int form
            nr_list.append(guess)
            ok_guess += 1
            if guess < nr:  #Om chansing lägre än nummer
                print('Guess too low!')
            elif guess > nr:    #Om chansing högre än nummer
                print('Guess too high!')
            else:   
                break
        if guess == nr: #Om chansning är lika med random nummer 
            print(f'Good {name}. You guessed right in {ok_guess} tries.')
        else:
            print(f'Too bad, number was {nr}')

        print(f'Guesss {"Value":>9}    Bar')    #Skapar en bar chart för listan 
        for index, value in enumerate(nr_list):
            print(f'{index:>5}{value:>13}{"*" * value}')

def main(): #En extra funktion, skapas för main method
    print('\nFucntion 1:\nShows 15 numbers from 1-1000 that are divisable with 4 and 9.\n')
    rnge()  #Kör funktion ett
    print('__________________________________________________________________________________')
    print('\nFunction 2:\nGuessing game 1-100.\n')
    guess() #Kör funktion två
    
if __name__ == "__main__":
    main() 