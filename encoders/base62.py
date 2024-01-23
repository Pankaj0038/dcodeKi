class Base62:
    BASE62_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def encode(num):
        if num == 0:
            return Base62.BASE62_ALPHABET[0]
        result = []
        base = len(Base62.BASE62_ALPHABET)
        while num:
            num, rem = divmod(num, base)
            result.append(Base62.BASE62_ALPHABET[rem])
        return ''.join(reversed(result))

    @staticmethod
    def decode(str):
        base = len(Base62.BASE62_ALPHABET)
        strlen = len(str)
        num = 0

        idx = 0
        for char in str:
            power = (strlen - (idx + 1))
            num += Base62.BASE62_ALPHABET.index(char) * (base ** power)
            idx += 1

        return num

# Example usage
original_number = 123456789
encoded_data = Base62.encode(original_number)
decoded_number = Base62.decode(encoded_data)

print("Original Number:", original_number)
print("Encoded Data:", encoded_data)
print("Decoded Number:", decoded_number)
