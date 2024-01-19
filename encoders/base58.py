#!/usr/bin/python

charset = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58_decode(ciphertext):
    result = 0
    for char in ciphertext:
        print(char)
        if char not in charset:
            raise ValueError(f"Invalid character '{char}' in Base58 input")
        print("character ",result)
        result = result * 58 + charset.index(char)
        print("result * 58 + index = ",result)

    result_bytes = bytearray()
    while result > 0:
        result_bytes.append(result % 256)
        print("bytes ",result_bytes)
        result //= 256
        print("result // 256 =  ",result)

    decoded_text = result_bytes[::-1].decode('utf-8')
    print(decoded_text)


def base58_encode(plaintext):
    cipher = ''
    num = int((''.join(["{0:08b}".format(ord(i)) for i in plaintext])),2)
    while num>= 58:
        cipher += charset[num%58]
        num//=58
        if num<=58: cipher+=charset[num]
    return cipher[::-1]


if __name__== "__main__":
    text_input = input("Enter a string: ")
    choice = input("Enter your choice (e for encode / d for decode): ")
    if choice == 'e':
        print(base58_encode(text_input))
    elif choice == 'd':
        print(base58_decode(text_input))
