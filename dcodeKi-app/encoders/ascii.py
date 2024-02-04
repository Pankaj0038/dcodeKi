def encode(plaintext):
    ciphertext = ""
    for char in plaintext:
        ciphertext += str(ord(char)) + " "
    return ciphertext.strip()

def decode(ciphertext):
    plaintext = ""
    encoded_chars = ciphertext.split()
    for encoded_char in encoded_chars:
        plaintext += chr(int(encoded_char))
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