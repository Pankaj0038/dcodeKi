##!usr/bin/python3

from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivymd.app import MDApp

from encoders import rot47,rot13,mybase64,mybase32, text2XOR2text, hex_encode ,  binary2text, text2binary, morse,atbash
from feature import c2c

#load the kv file 
Builder.load_file('dcodeKi.kv')

class DcodLayout(Widget):

	#create an object property to store the input
	cipher = ObjectProperty(None)

	#create an object property to store the key
	cipher_key = ObjectProperty(None)

	#string to store encoded/decoded text
	decoded = ""

	def __init__(self,**kwargs):
		super(DcodLayout,self).__init__(**kwargs)

	#fuction which define the functionality of the buttons
	def press(self,method):
		global decoded

		#on button press store the input field in cipher object
		cipher = self.cipher.text
		cipher_key = self.cipher_key.text
		
		#match case for multiple encoders/decoders (match the button (which is pressed) and apply function according to it)
		match method:
			case 'b64':
				decoded = mybase64.decode(cipher) #button == base64 decode 

			case 'b64e':
				decoded = mybase64.encode(cipher)

			case 'rot13':
				decoded = rot13.rot13(cipher)

			case 'rot47':
				decoded = rot47.rot47(cipher)

			case 'b32':
				decoded = mybase32.decode(cipher)

			case 'b32e':
				decoded = mybase32.encode(cipher)
			
			case 't2b':
				decoded = text2binary.encode(cipher)
			
			case 'b2t' :
				decoded = binary2text.decode(cipher)

			case "text2XOR2text":
				decoded = text2XOR2text.encode(cipher,cipher_key)

			case "hex_encode":
				decoded = hex_encode.encode(cipher)

			case "hex_decode":
				decoded = hex_encode.decode(cipher)

			case "morse_encode":
				decoded = morse.encode(cipher)

			case "morse_decode":
				decoded = morse.decode(cipher)

			case "atci":
				decoded = atbash.decatbash(cipher)

			case "vigenere_encode":
				decoded = vigenere.encode(cipher, cipher_key)

			case "vigenere_decode":
				decoded = vigenere.decode(cipher, cipher_key)


		#replace the text in id="string" by the value of the "decoded" variable
		self.ids.string.text = f'{decoded}'
		#after printing the output clear the input field
		self.cipher.text=''
		self.cipher_key.text=''

	def copy(self):
		try:
			c2c.copy(decoded)
		except:
			self.ids.string.text = "Nothing to copy!"

#App building
class DcodeKiApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		return DcodLayout()

#If executes this file then run the program 
if __name__ == '__main__':
	DcodeKiApp().run()
