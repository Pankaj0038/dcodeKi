#!/usr/bin/env python3


def encode(plaintext):
    ciphertext = ""

    for char in plaintext:
        ciphertext += oct(ord(char)).lstrip("0o")+" "

    return ciphertext


def decode(ciphertext):
    plaintext = ""
    
    for char in ciphertext.split():
        plaintext += chr(int(char, 8))

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