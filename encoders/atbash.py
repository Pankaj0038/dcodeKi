def decatbash(message):
    cipher = ''
    for letter in message.upper():
        ascii = ord(letter)
        if 65 <= ascii <= 90:
            position = ascii - 65
            newpos = 25 - position
            newAscii = newpos + 65
            newLetter = chr(newAscii)
        else:
            newLetter = letter
        cipher = cipher + newLetter
    return cipher
