#!/usr/bin/env python3


morse = {
    "A": ".-"   ,
    "B": "-..." ,
    "C": "-.-." ,
    "D": "-.."  ,
    "E": "."    ,
    "F": "..-." ,
    "G": "--."  ,
    "H": "...." ,
    "I": ".."   ,
    "J": ".---" ,
    "K": "-.-"  ,
    "L": ".-.." ,
    "M": "--"   ,
    "N": "-."   ,
    "O": "---"  ,
    "P": ".--." ,
    "Q": "--.-" ,
    "R": ".-."  ,
    "S": "..."  ,
    "T": "-"    ,
    "U": "..-"  ,
    "V": "..._" ,
    "W": ".--"  ,
    "X": "-..-" ,
    "Y": "-.--" ,
    "Z": "--.." ,
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}


def encode(plaintext):
    ciphertext = ""

    for char in plaintext:
        if char != " ":
            ciphertext += morse[char.upper()]+" "

    return ciphertext


def decode(ciphertext):
    plaintext = ""
    ciphertext = ciphertext.replace("_", "-")
    morse_char_list = ciphertext.split()

    for morse_char in morse_char_list:
        for char in morse:
            if morse[char] == morse_char:
                plaintext += char

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