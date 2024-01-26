import binascii

BASE62_CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
encoding_chunk_size = 2
decoding_chunk_size = 3


def encode(input_str):
    encoded = []

    in_bytes = bytearray(input_str, 'utf-8')
    byte_length = len(in_bytes)

    for i in range(0, byte_length, encoding_chunk_size):
        chunk = in_bytes[i:min(i + encoding_chunk_size, byte_length)]
        s = binascii.hexlify(chunk).decode('utf-8')
        val = int(s, 16)

        w = ""
        while val:
            val, remainder = divmod(val, 62)
            w = BASE62_CHARSET[remainder] + w

        w = '0' * (decoding_chunk_size - len(w)) + w
        encoded.append(w)
    return ''.join(encoded)


def decode(encoded):
    decoded_bytes = bytearray()
    for i in range(0, len(encoded), decoding_chunk_size):
        chunk = encoded[i:min(i + decoding_chunk_size, len(encoded))]
        val = from_base62(chunk)
        chunk_hex = format(val, 'x')
        try:
            dst = binascii.unhexlify(chunk_hex.encode('utf-8'))
        except binascii.Error as e:
            return f"The given input '{encoded}' is not a valid base62 string"
            raise ValueError("malformed input") from e
        decoded_bytes.extend(dst)
    return decoded_bytes.decode('utf-8')


def from_base62(s):
    result = 0
    for char in s:
        result = result * 62 + BASE62_CHARSET.index(char)
    return result



# if __name__ == "__main__":
#     test_data = [
#         "Hello World", 
#         "base-62",
#     ]
    
#     for data in test_data:
#         if decode(encode(data)) != data:
#             print("Error for data:", data)
#     else:
#         print("All tests passed!!")

#     usr_input = input("Enter the string to be encoded/decoded: ")
#     op = input("Enter 'e' for encode and 'd' for decode: ")
#     if op == "e":
#         print(encode(usr_input))
#     elif op == "d":
#         print(decode(usr_input))
#     else:
#         print("Invalid option")
