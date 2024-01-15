##!/usr/bin/python
import string
alp = string.ascii_lowercase
ALP = string.ascii_uppercase
def decatbash(message):
    cipher = ''
    for letter in message:
        if letter in ALP:
            ascii = ord(letter)
            if 65 <= ascii <= 90:
                position = ascii - 65
                newpos = 25 - position
                newAscii = newpos + 65
                newLetter = chr(newAscii)
        elif letter in alp:
            ascii = ord(letter)
            if 97 <= ascii <= 122:
                position = ascii - 97
                newpos = 25 - position
                newAscii = newpos + 97
                newLetter = chr(newAscii)
        else:
            newLetter = letter
        cipher += newLetter
    return cipher
