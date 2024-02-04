#!/usr/bin/env python3

def binary_to_gray(n):
    n = int(n, 2)
    n ^= (n >> 1)
    return bin(n)[2:]

def gray_to_binary(n):
    n = int(n, 2)
    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask
    return bin(n)[2:]

def encode(plaintext):
    ciphertext = ""
    for char in plaintext:
        binary = format(ord(char), '08b')
        gray = binary_to_gray(binary)
        ciphertext += gray + " "
    return ciphertext

def decode(ciphertext):
    plaintext = ""
    for char in ciphertext.split():
        binary = gray_to_binary(char)
        plaintext += chr(int(binary, 2))
    return plaintext

def main():
    text = input("Enter the text to be encoded/decoded: ")
    option = input("Encode/Decode? (e/d): ")

    if option == "e":
        ciphertext = encode(text)
        print(ciphertext)
    elif option == "d":
        plaintext = decode(text)
        print(plaintext)
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()