'''
ceasar.py
https://commons.wikimedia.org/wiki/File:ASCII-Table-wide.svg
'''
from myhashcalc import hashcalc

A_UC = 65
A_LC = 97
NUM_CHARS = 26

def encrypt(plain, rot):
    '''ceasar encrypt'''
    result = ""
    # enumerate the plain text
    for i, char in enumerate(plain):
        if char.isalpha():
            # Encrypt uppercase characters in plain text
            if (char.isupper()):
                result += chr((ord(char) + rot - A_UC) % NUM_CHARS + A_UC)
            # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) + rot - A_LC) % NUM_CHARS + A_LC)
        else:
            result += char

    return result

def decrypt(cipher, rot):
    '''ceasar decrypt'''
    result = ""
    # enumerate the cipher text
    for i, char in enumerate(cipher):
        if char.isalpha():
            # Decrypt uppercase characters in cipher text
            if (char.isupper()):
                result += chr((ord(char) - rot + A_UC) % NUM_CHARS + A_UC)
            # Decrypt lowercase characters in cipher text
            else:
                result += chr((ord(char) - rot + A_LC) % NUM_CHARS + A_LC)
        else:
            result += char

    return result

if __name__ == "__main__":
    # Must use either only upper or lower chars!
    text = "CAESAR CIPHER DEMO"
    shift = 15
    algo = 'sha1'

    # calculate hash
    print(f"Before: {hashcalc(text.encode('ascii'), algo)}")
    print(f'Plain: {text}')
    print(f'Shift pattern: {str(shift)}')
    encrypted = encrypt(text, shift)
    print(f'Cipher: {encrypted}')
    decrypted = decrypt(encrypted, shift)
    print(f'Plain: {decrypted}')
    print(f"After: {hashcalc(decrypted.encode('ascii'), algo)}")

    with open('Ceasar.txt', 'w') as newFile:
        newFile.write(f"Before: {hashcalc(text.encode('ascii'), algo)}")
        newFile.write(f'\nPlain: {text}')
        newFile.write(f'\nShift pattern: {str(shift)}')
        newFile.write(f'\nCipher: {encrypted}')
        newFile.write(f'\nPlain: {decrypted}')
        newFile.write(f"\nAfter: {hashcalc(decrypted.encode('ascii'), algo)}")