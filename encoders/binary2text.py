#!/usr/bin/python3

def _binary2text(s):
  binlist = s.split(" ")  
  return ''.join(chr(int(i,2)) for i in binlist)

def binary2text(s):
  return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def decode(b):
    if " " in b:
      bin = b.strip()
      text = _binary2text(b)
    else :
      text = binary2text(b)
    return text

if __name__ == '__main__':
  binarytext = input("Enter a binary to decode: ")
  print(decode(binarytext))
