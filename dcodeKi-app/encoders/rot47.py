#!/usr/bin/python

def rot47(flag):
	li = []
	for i in range(33,127):
	    li.append(chr(i))
	enc = ''
	for char in flag:
	    enc += li[((ord(char)-33)+47)%94]
	return enc 
if __name__ == '__main__':
    ptext = input("Enter a string to encode or decode: ")
    print(rot47(ptext))