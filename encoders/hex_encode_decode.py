#!/usr/bin/env python3


def encode(plaintext):
    ciphertext = ""

    for char in plaintext:
        ciphertext += hex(ord(char)).lstrip("0x")

    return ciphertext


def decode(ciphertext):
    plaintext = ""
    ciphertext = ciphertext.replace(" ", "")

    for i in range(0, len(ciphertext), 2):
        char = ciphertext[i]+ciphertext[i+1]

        plaintext += chr(int(char, 16))

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