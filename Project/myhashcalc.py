'''myhashcalc.py
Common encrypt and decryption functions
'''
import hashlib

def hashcalc(buf, algorthm):
    '''Hash in Python a buffert'''
    if algorthm == 'md5':
        hasher = hashlib.md5()
    elif algorthm == 'sha1':
        hasher = hashlib.sha1()
    hasher.update(buf)
    return hasher.hexdigest()
