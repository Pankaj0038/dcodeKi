#!/usr/bin/python3
def encode(flag):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    enc = ''
    binary_string=''
    for char in flag:
        binary_string += "{0:08b}".format(ord(char))
    chunks = [binary_string[i:i+5] for i in range(0,len(binary_string),5)]
    if len(chunks[-1]) < 5:
        x = 5 - len(chunks[-1])
        chunks[-1] = "{0:05b}".format(int(chunks[-1],2) << x)
    encoded_string = ''
    for i in chunks:
        encoded_string  += alpha[int(i,2)]
    return encoded_string


def decode(enc):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    flag=''
    binary = ''
    li=[]
    for ind in range(len(enc)):
        for i in range(len(alpha)):
            if enc[ind] == alpha[i]:
                li.append(str(i))
    for num in li:
        binary += "{0:05b}".format(int(num))
    chunks = [binary[i:i+8] for i in range(0,len(binary),8)]
    for i in chunks:
        flag += chr(int(i,2))
    return flag
if __name__ == '__main__':
    ptext = input("Enter a string to encode or decode: ")
    op = input("Do you want to encode it or decode (e/d): ")
    if op=="e":
        print(encode(ptext))
    elif op=="d":
        print(decode(ptext))
    else:
        print("Invalid Option!")