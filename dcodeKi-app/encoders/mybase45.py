charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"

def encode(to_encode):
	to_encode = to_encode.encode()
	res = ""
	i = 0
	while i < len(to_encode):
		if i % 2 == 0 and len(to_encode) - i >= 2:
			x = (to_encode[i] << 8) + to_encode[i + 1]
			e, x = divmod(x, 45 * 45)
			d, c = divmod(x, 45)
			res += charset[c] + charset[d] + charset[e]
		i += 2

	if len(to_encode) % 2 == 1:
		d, c = divmod(to_encode[-1], 45)
		res += charset[c] + charset[d]
	return res


def decode(to_decode):
	to_decode = [charset.index(c) for c in to_decode]
	if len(to_decode) % 3 == 1:
		return f"Invalid base45 string '{to_decode}'"

	res = []
	i = 0
	while i < len(to_decode):
		if len(to_decode) - i >= 3:
			x = to_decode[i] + to_decode[i + 1] * 45 + to_decode[i + 2] * 45 * 45
			if x > 65535:
				return f"Invalid base45 input '{to_decode}'"
			res.extend(divmod(x, 256))
		else:
			x = to_decode[i] + to_decode[i + 1] * 45
			if x > 255:
				return f"Invalid base45 input '{to_decode}'"
			res.append(x)
		i += 3
	return bytes(res).decode()


# if __name__ == "__main__":
# 	usr_input = input("Enter a string to encode or decode: ")
# 	op = input("Do you want to encode it or decode (e/d): ")
# 	if op == "e":
# 		print(encode(usr_input))
# 	elif op == "d":
# 		print(decode(usr_input))
# 	else:
# 		print("Invalid Option!")
