def custom_xor(char, key):
    return chr(ord(char) ^ key)

def xor_brute_force(text):
    results = []
    for key in range(1, 256):
        decoded = "".join([custom_xor(char, key) for char in text])
        results.append((key, decoded))
    return results

if __name__ == '__main__':
    ptext = input("Enter a string to encode or decode: ")
    print(xor_brute_force(ptext))
