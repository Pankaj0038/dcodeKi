#!/usr/bin/python

alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13(enc_str):
    flag = ''
    for char in enc_str:
        if ord(char) >= 65 and ord(char) <=90:
            index = ((ord(char) - 65) + 13) % len(ALPHA)
            flag += ALPHA[index]
        elif  ord(char) >=97 and ord(char) <= 122:
            index = ((ord(char)-97)+13) % len(alpha)
            flag += alpha[index]
        else:
            flag += char
    return flag
if __name__ == '__main__':
    ptext = input("Enter a string to encode or decode: ")
    print(rot13(ptext))