from encoders.rot13 import rot13


def rot13_brute_force(text):
    results = []
    for shift in range(1, 26):
        decoded = rot13.rot13(text, shift)
        results.append((shift, decoded))
    return results

if __name__ == "__main__":
    main()
