

def xor_brute_force(text):
    results = []
    for key in range(256):
        decoded = text2XOR2text.decode(text, key)
        results.append((key, decoded))
    return results



if __name__ == "__main__":
    main()