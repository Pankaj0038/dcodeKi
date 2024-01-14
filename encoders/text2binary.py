#!/usr/bin/env python3


def encode(plaintext):
    ciphertext = ""

    for char in plaintext:
        ciphertext += format(ord(char), "08b")+" "

    return ciphertext


def main():
    plaintext = input("Enter the text to be encoded: ")
    ciphertext = encode(plaintext)
    print(ciphertext)


if __name__ == "__main__":
    main()