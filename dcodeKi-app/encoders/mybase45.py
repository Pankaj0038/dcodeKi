BASE45_CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"

def encode(to_encode):
	to_encode = to_encode.encode()
	res = ""
	i = 0
	while i < len(to_encode):
		if i % 2 == 0 and len(to_encode) - i >= 2:
			x = (to_encode[i] << 8) + to_encode[i + 1]
			e, x = divmod(x, 45 * 45)
			d, c = divmod(x, 45)
			res += BASE45_CHARSET[c] + BASE45_CHARSET[d] + BASE45_CHARSET[e]
		i += 2

	if len(to_encode) % 2 == 1:
		d, c = divmod(to_encode[-1], 45)
		res += BASE45_CHARSET[c] + BASE45_CHARSET[d]
	return res


if __name__ == "__main__":
	ptext = input("Enter a string to encode or decode: ")
	op = input("Do you want to encode it or decode (e/d): ")
	if op == "e":
		print(encode(ptext))
	elif op == "d":
		pass
	else:
		print("Invalid Option!")
