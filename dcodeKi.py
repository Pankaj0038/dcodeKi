#!usr/bin/python3

from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from encoders import rot47,rot13,mybase64,mybase32, hex_encode_decode
from feature import c2c

#load the kv file 
Builder.load_file('dcodeKi.kv')

class DcodLayout(Widget):

	#create an object property to store the input
	cipher = ObjectProperty(None)

	def __init__(self,**kwargs):
		super(DcodLayout,self).__init__(**kwargs)
	
	#fuction which define the functionality of the buttons
	def press(self,method):

		#on button press store the input field in cipher object
		cipher = self.cipher.text
		
		#match case for multiple encoders/decoders (match the button (which is pressed) and apply function according to it)
		match method:
			case 'b64':
				decoded = mybase64.decode(cipher) #button == base64 decode 
				c2c.copy(decoded) #copy to clipboard

			case 'b64e':
				decoded = mybase64.encode(cipher)
				c2c.copy(decoded)

			case 'rot13':
				decoded = rot13.rot13(cipher)
				c2c.copy(decoded)

			case 'rot47':
				decoded = rot47.rot47(cipher)
				c2c.copy(decoded)

			case 'b32':
				decoded = mybase32.decode(cipher)
				c2c.copy(decoded)

			case 'b32e':
				decoded = mybase32.encode(cipher)
				c2c.copy(decoded)

			case "hex_encode":
				decoded = hex_encode_decode.encode(cipher)
				c2c.copy(decoded)

			case "hex_decode":
				decoded = hex_encode_decode.decode(cipher)
				c2c.copy(decoded)

		#replace the text in id="string" by the value of the "decoded" variable
		self.ids.string.text = f'{decoded}'
		#after printing the output clear the input field
		self.cipher.text=''

#App building
class DcodeKiApp(App):
	def build(self):
		return DcodLayout()

#If executes this file then run the program 
if __name__ == '__main__':
	DcodeKiApp().run()
