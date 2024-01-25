class Base45:
    BASE45_CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"

    @staticmethod
    def encode(data):
        result = []
        data_len = len(data)
        for i in range(0, data_len, 2):
            if i + 1 < data_len:
                x = (data[i] << 8) + data[i+1]
                result.append(Base45.BASE45_CHARSET[x % 45])
                result.append(Base45.BASE45_CHARSET[(x // 45) % 45])
                result.append(Base45.BASE45_CHARSET[x // (45*45)])
            else:
                x = data[i]
                result.append(Base45.BASE45_CHARSET[x % 45])
                result.append(Base45.BASE45_CHARSET[x // 45])

        return ''.join(result).rstrip('\0')

    @staticmethod
    def decode(data):
        result = bytearray()
        data_len = len(data)
        for i in range(0, data_len, 3):
            x = Base45.BASE45_CHARSET.index(data[i]) + Base45.BASE45_CHARSET.index(data[i+1]) * 45
            if i + 2 < data_len:
                x += Base45.BASE45_CHARSET.index(data[i+2]) * 45 * 45
                result.append(x >> 8)
            result.append(x & 0xFF)

        return bytes(result)

print("Original Data:", original_data)
print("Encoded Data:", encoded_data)
print("Decoded Data:", decoded_data.decode())
