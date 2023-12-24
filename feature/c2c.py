import pyperclip

def copy(text):
	pyperclip.copy(text) #Copy to clipboard function
	spam = pyperclip.paste()

if __name__ == '__main__':
	txt=input("Enter a text to copy: ")
	copy(txt)
