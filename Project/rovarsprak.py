'''rovarsprak.py'''

from myhashcalc import hashcalc

# globals
CONSONANTS = 'bcdfghjklmnpqrstvwxz'

def enc_rov(item):
    '''encode to rovar'''
    for c in CONSONANTS.lower():
        item = item.replace(c, f'{c}o{c}')
    for c in CONSONANTS.upper():
        item = item.replace(c, f'{c}O{c}')
    return item

def dec_rov(item):
    '''decode from rovar'''
    for c in CONSONANTS.lower():
        item = item.replace(f'{c}o{c}', c)
    for c in CONSONANTS.upper():
        item = item.replace(f'{c}O{c}', c)
    return item

if __name__ == "__main__":
    # print(enc_rov('poppen'))
    # print(dec_rov('popopoppopenon'))

    algo = 'sha1'
    message = str(input('poppen'))
    print(f"Before: {hashcalc(message.encode('ascii'), algo)}")
    print(f'Sending: {message}')
    message = enc_rov(message)
    print(f'Received: {message}')
    message = dec_rov(message)
    print(f'Verifying: {message}')
    print(f"After: {hashcalc(message.encode('ascii'), algo)}")

    with open('Rovarsprak.txt', 'w') as newFile:
        newFile.write(f"\nBefore: {hashcalc(message.encode('ascii'), algo)}")
        newFile.write(f'\nSending: {message}')
        newFile.write(f'\nReceived: {message}')
        newFile.write(f'\nVerifying: {message}')
        newFile.write(f"\nAfter: {hashcalc(message.encode('ascii'), algo)}")