import binascii

charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encode(input_str):
    encoded = []
    in_bytes = bytearray(input_str, 'utf-8')
    byte_length = len(in_bytes)
    i = 0
    while i < byte_length:
        chunk = in_bytes[i:min(i + 2, byte_length)]
        s = binascii.hexlify(chunk).decode()
        val = int(s, 16)
        w = ""
        while val:
            val, remainder = divmod(val, 62)
            w = charset[remainder] + w
        w = '0' * (3 - len(w)) + w
        encoded.append(w)
        i += 2
    return ''.join(encoded)


# if __name__ == "__main__":
#     usr_input = input("Enter the string to be encoded/decoded: ")
#     op = input("Enter 'e' for encode and 'd' for decode: ")
#     if op == "e":
#         print(encode(usr_input), decode(encode(usr_input)))
#     elif op == "d":
#         print(decode(usr_input))
#     else:
#         print("Invalid option")
