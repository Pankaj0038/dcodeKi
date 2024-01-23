#!/usr/bin/python3

def encode(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

def decode(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext

if __name__ == '__main__':
    ptext = input("Enter a string to encode or decode: ")
    key = input("Enter the key")
    op = input("Do you want to encode it or decode (e/d): ")
    if op=="e":
        print(encode(ptext, key))
    elif op=="d":
        print(decode(ptext, key))
    else:
        print("Invalid Option!")