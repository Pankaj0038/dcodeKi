#!/usr/bin/env python3

leet = {
    "A": "4",
    "B": "8",
    "E": "3",
    "G": "6",
    "I": "1",
    "O": "0",
    "S": "5",
    "T": "7",
    "L": "1",
    "Z": "2",
    " ": " "
}

def encode(plaintext):
    ciphertext = ""

    for char in plaintext:
        if char.upper() in leet:
            ciphertext += leet[char.upper()]
        else:
            ciphertext += char

    return ciphertext

def decode(ciphertext):
    plaintext = ""
    for char in ciphertext:
        for key, value in leet.items():
            if char == value:
                plaintext += key
                break
        else:
            plaintext += char

    return plaintext

def main():
    text = input("Enter the text to be encoded/decoded: ")
    option = input("Encode/Decode? (e/d): ")

    if option.lower() == "e":
        ciphertext = encode(text)
        print(ciphertext)
    elif option.lower() == "d":
        plaintext = decode(text)
        print(plaintext)
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()