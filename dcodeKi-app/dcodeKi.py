##!usr/bin/python3
#import all the important modules
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock

from encoders import rot47, rot13, mybase64, mybase32,extra, text2XOR2text, hex_encode, binary2text, text2binary, morse, atbash, octal, rot8000, vigenere, base58, mybase45, mybase62
from feature import c2c

#load the kv file 
Builder.load_file('dcodeKi.kv')

class DcodLayout(Screen):

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
			case 'b45':
				decoded = mybase45.decode(cipher) #button == mybase45 decode
			
			case 'b45e':
				decoded = mybase45.encode(cipher) #button == mybase45 encode
			
			case 'b62':
				decoded = mybase62.decode(cipher) #button == mybase62 decode
			
			case 'b62e':
				decoded = mybase62.encode(cipher)
			
			case 'b64':
				decoded = mybase64.decode(cipher) #button == base64 decode 

			case 'b64e':
				decoded = mybase64.encode(cipher)#button == base64 encode 

			case 'rot13':
				decoded = rot13.rot13(cipher)#button == ROT13 code 

			case 'rot47':
				decoded = rot47.rot47(cipher) #button == ROT47 code 

			case 'b32':
				decoded = mybase32.decode(cipher)#button == base32 decode 

			case 'b32e':
				decoded = mybase32.encode(cipher)#button == base32  encode 
			
			case 't2b':
				decoded = text2binary.encode(cipher)#button == binary code for text 
			
			case 'b2t' :
				decoded = binary2text.decode(cipher)#button =text code to binary 

			case "text2XOR2text":
				decoded = text2XOR2text.encode(cipher,cipher_key)

			case "hex_encode":
				decoded = hex_encode.encode(cipher)#button == hex encode 

			case "hex_decode":
				decoded = hex_encode.decode(cipher)#button == base64 decode 

			case "morse_encode":
				decoded = morse.encode(cipher)#button == Morse encode 

			case "morse_decode":
				decoded = morse.decode(cipher)#button == Morse decode 

			case "atci":
				decoded = atbash.decatbash(cipher)

			case "vigenere_encode":
				decoded = vigenere.encode(cipher, cipher_key)#button == Vigenere encode 

			case "vigenere_decode":
				decoded = vigenere.decode(cipher, cipher_key)#button == Vigenere decode 

			case "octal_encode":
				decoded = octal.encode(cipher)#button == octal encode 

			case "octal_decode":
				decoded = octal.decode(cipher)#button == octal decode 

			case "rot8000_encode":
				decoded = rot8000.encode(cipher)#button == ROT8000 encode 

			case "rot8000_decode":
				decoded = rot8000.decode(cipher)#button == ROT8000 decode 

			case "base58d":
				decoded = base58.base58_decode(cipher)#button == base58d decode 
			
			case "base58e":
				decoded = base58.base58_encode(cipher) #button == base58d encode 
			
			case "upper":
				decoded = extra.Upper(cipher)
			
			case "lower":
				decoded = extra.Lower(cipher)
			
			case "reverse":
				decoded = extra.Reverse(cipher)


		#replace the text in id="string" by the value of the "decoded" variable
		self.ids.string.text = f'{decoded}'
		#after printing the output clear the input field
		self.cipher.text=''
		self.cipher_key.text=''

	def copy(self):
		try:
			c2c.copy(decoded)# copy to clipboard
		except:
			self.ids.string.text = "Nothing to copy!"

#App building
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

class DcodeKiApp(MDApp):
    def build(self):
        self.icon = "logo.png"
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("splash.kv"))
        sm.add_widget(DcodLayout(name='main'))
        return sm

    def on_start(self):
        # Schedule the transition to the main screen after 5 seconds
        Clock.schedule_once(self.show_main_screen, 5)

    def show_main_screen(self, dt):
        sm = self.root
        sm.current = 'main'

# If executing this file, then run the program
if __name__ == '__main__':
	DcodeKiApp().run()