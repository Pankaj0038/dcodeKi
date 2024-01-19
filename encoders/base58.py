#!/usr/bin/python

charset = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58_decode(ciphertext):
    result = 0
    for char in ciphertext:
        if char not in charset:
            raise ValueError(f"Invalid character '{char}' in Base58 input")
        result = result * 58 + charset.index(char)

    result_bytes = bytearray()
    while result > 0:
        result_bytes.append(result % 256)
        result //= 256

    decoded_text = result_bytes[::-1].decode('utf-8')
    return decoded_text
