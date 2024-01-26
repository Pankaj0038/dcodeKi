BASE45_CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"
BASE45_DICT = {v: i for i, v in enumerate(BASE45_CHARSET)}


def encode(to_encode: str) -> str:
    to_encode = to_encode.encode()
    res = ""

    for i in range(0, len(to_encode) & ~1, 2):
        x = (to_encode[i] << 8) + to_encode[i + 1]
        e, x = divmod(x, 45 * 45)
        d, c = divmod(x, 45)
        res += BASE45_CHARSET[c] + BASE45_CHARSET[d] + BASE45_CHARSET[e]
    if len(to_encode) & 1:
        d, c = divmod(to_encode[-1], 45)
        res += BASE45_CHARSET[c] + BASE45_CHARSET[d]
    
    return res


def decode(to_decode) -> str:
    try:
        if isinstance(to_decode, str):
            to_decode = [BASE45_DICT[c] for c in to_decode.rstrip("\n")]
        elif isinstance(to_decode, bytes):
            to_decode = [BASE45_DICT[c] for c in to_decode.decode()]
        else:
            raise TypeError("Type must be 'str' or 'bytes'")

        if len(to_decode) % 3 == 1:
            raise ValueError("Invalid base45 string")

        res = []
        for i in range(0, len(to_decode), 3):
            if len(to_decode) - i >= 3:
                x = to_decode[i] + to_decode[i + 1] * 45 + to_decode[i + 2] * 45 * 45
                if x > 0xFFFF:
                    raise ValueError
                res.extend(divmod(x, 256))
            else:
                x = to_decode[i] + to_decode[i + 1] * 45
                if x > 0xFF:
                    raise ValueError
                res.append(x)

        return bytes(res).decode()
    except (ValueError, KeyError, AttributeError):
        return f"The given input '{to_decode}' is not a valid base45 string"
        raise ValueError("Invalid string to be decoded", to_decode)



# if __name__ == "__main__":
#     test_data = [
#         "Hello World", 
#         "base-62",
#     ]
# 
#     for data in test_data:
#         if decode(encode(data)) != data:
#             print("Error for data:", data)
#     else:
#         print("All tests passed!!")
# 
#     usr_input = input("Enter the string to be encoded/decoded: ")
#     op = input("Enter 'e' for encode and 'd' for decode: ")
#     if op == "e":
#         print(encode(usr_input))
#     elif op == "d":
#         print(decode(usr_input))
#     else:
#         print("Invalid option")
