def encode(plaintext):
    """
    This function takes a plaintext string and encodes it into a URL safe format.
    It iterates over each character in the plaintext string and checks if it is alphanumeric or one of the special characters.
    If it is, it adds the character to the ciphertext string.
    If it is not, it converts the character to its hexadecimal representation and adds it to the ciphertext string.
    Spaces are replaced with '%20'.

    Args:
        plaintext (str): The plaintext string to be encoded.

    Returns:
        str: The URL encoded string (ciphertext).
    """
    ciphertext = ""
    
    for char in plaintext:
        if char.isalnum() or char in ['-', '_', '.', '~']:
            ciphertext += char
        elif char == ' ':
            ciphertext += '%20'
        else:
            ciphertext += '%' + hex(ord(char))[2:].upper()
    
    return ciphertext


def decode(ciphertext):
    """
    This function takes a URL encoded string (ciphertext) and decodes it back into plaintext.
    It iterates over each character in the ciphertext.
    If it encounters a '%', it treats the next two characters as a hexadecimal number and converts it back into a character.
    If it does not encounter a '%', it adds the character to the plaintext string.
    '%20' is replaced with a space.

    Args:
        ciphertext (str): The URL encoded string to be decoded.

    Returns:
        str: The decoded plaintext string.
    """
    plaintext = ""
    
    i = 0
    while i < len(ciphertext):
        if ciphertext[i] == '%':
            if i + 2 < len(ciphertext):
                if ciphertext[i+1:i+3] == '20':
                    plaintext += ' '
                else:
                    plaintext += chr(int(ciphertext[i+1:i+3], 16))
                i += 3
            else:
                raise ValueError("Invalid ciphertext")
        else:
            plaintext += ciphertext[i]
            i += 1
    
    return plaintext


def main():
    """
    This is the main function that prompts the user for input and calls the appropriate function based on the user's choice.
    """
    text = input("Enter the plaintext to be encoded or ciphertext to be decoded: ")
    option = input("Encode or Decode? (Enter 'e' for encode or 'd' for decode): ")

    if option.lower() == "e":
        ciphertext = encode(text)
        print(f"Ciphertext: {ciphertext}")
    elif option.lower() == "d":
        try:
            plaintext = decode(text)
            print(f"Plaintext: {plaintext}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid option! Please enter 'e' for encode or 'd' for decode.")


if __name__ == "__main__":
    main()