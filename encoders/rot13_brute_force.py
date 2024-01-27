def custom_rot13(char, shift):
    if char.isalpha():
        start = ord('a') if char.islower() else ord('A')
        return chr((ord(char) - start + shift) % 26 + start)
    return char

def rot13_brute_force(text):
    results = []
    for shift in range(1, 26):
        decoded = "".join([custom_rot13(char, shift) for char in text])
        results.append((shift, decoded))
    return results

if __name__ == '__main__':
    ptext = input("Enter a string to encode or decode: ")
    print(rot13_brute_force(ptext))
