#!/usr/bin/env python3
from urllib.parse import quote_plus
from urllib.parse import unquote_plus

def encode(plaintext):
    ciphertext = quote_plus(plaintext)
    return ciphertext


def decode(ciphertext):
    plaintext = unquote_plus(ciphertext)
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