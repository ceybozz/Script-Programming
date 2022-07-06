'''reverse.py'''
from myhashcalc import hashcalc

def reverse(item):
    '''message to reverse'''
    i = len(str(item)) - 1
    rev_txt = str('') # cipher text is stored in this variable
    while i >= 0:
        rev_txt += str(item[i])
        i -= 1
    return rev_txt

if __name__ == "__main__":
    algo = 'sha1'
    message = str(input('Text to Reverse: '))
    print(f"Before: {hashcalc(message.encode('ascii'), algo)}")
    print(f'Sending: {message}')
    message = reverse(message)
    print(f'Received: {message}')
    message = reverse(message)
    print(f'Verifying: {message}')
    print(f"After: {hashcalc(message.encode('ascii'), algo)}")

    with open('Reverse.txt', 'w') as newFile:
        newFile.write(f"\nBefore: {hashcalc(message.encode('ascii'), algo)}")
        newFile.write(f'\nSending: {message}')
        newFile.write(f'\nReceived: {message}')
        newFile.write(f'\nVerifying: {message}')
        newFile.write(f"\nAfter: {hashcalc(message.encode('ascii'), algo)}")