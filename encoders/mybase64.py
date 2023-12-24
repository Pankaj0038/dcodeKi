#!/usr/bin/python3

def decode(enc):
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    li = []
    for i in range(0,len(enc)):
        for j in range(0,len(char)):
            if enc[i] == char[j]:
                li.append(str(j))
    binary = ''
    flag =''
    for num in li:
        binary += "{0:06b}".format(int(num))
    chunks = [binary[i:i+8] for i in range(0,len(binary),8)]
        
    for i in chunks:
        flag += chr(int(i,2))
    return flag

def encode(flag):
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    enc=''
    binary_string =''
    for letter in flag:
        binary_string += "{0:08b}".format(ord(letter))
    chunks = [binary_string[i:i+6] for i in range(0,len(binary_string),6)]
    for i in range(len(chunks)):
        if len(chunks[i]) < 6:
            x = 6 - len(chunks[i])
            chunks[i] = "{0:06b}".format(int(chunks[i],2) << x)
    encoded_string = ''
    for i in chunks:
        encoded_string += char[int(i,2)]
    return encoded_string
if __name__ == '__main__':
    ptext = input("Enter a string to encode or decode: ")
    op = input("Do you want to encode it or decode (e/d): ")
    if op=="e":
        print(encode(ptext))
    elif op=="d":
        print(decode(ptext))
    else:
        print("Invalid Option!")
