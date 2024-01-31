#!/usr/bin/python3
#import all the important modules
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock

from encoders import rot47, rot13, mybase64, mybase32,extra, text2XOR2text, hex_encode, binary2text, text2binary, morse, atbash, octal, rot8000, vigenere, base58, mybase45, mybase62, url, leet
from feature import c2c

import logging

# Configure logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

#load the kv file 
Builder.load_file('dcodeKi.kv')

# Setting up the window size and position
Window.size = (850, 930)
Window.top = 100

class DcodLayout(Screen):

	#create an object property to store the input
	cipher = ObjectProperty(None)

	#create an object property to store the key
	cipher_key = ObjectProperty(None)

	#string to store encoded/decoded text
	decoded = ""

	def __init__(self,**kwargs):
		super(DcodLayout,self).__init__(**kwargs)
	def open_symbol_cipher_page(self):
		app = MDApp.get_running_app()
		app.root.current = 'symbol_cipher_page'

	#fuction which define the functionality of the buttons
	def press(self,method):
		global decoded

		#on button press store the input field in cipher object
		cipher = self.cipher.text
		cipher_key = self.cipher_key.text
		
		#match case for multiple encoders/decoders (match the button (which is pressed) and apply function according to it)
		match method:
			case 'b45':
				try:
					decoded = mybase45.decode(cipher) #button == mybase45 decode
				except Exception as e:
					logger.error("An error occurred while decoding with base45: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with base45: " + str(e)
					raise
			
			case 'b45e':
				try:
					decoded = mybase45.encode(cipher) #button == mybase45 encode
				except Exception as e:
					logger.error("An error occurred while encoding with base45: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with base45: " + str(e)
					raise

			case 'b62':
				try:
					decoded = mybase62.decode(cipher) #button == mybase62 decode
				except Exception as e:
					logger.error("An error occurred while decoding with base62: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with base62: " + str(e)
					raise
			
			case 'b62e':
				try:
					decoded = mybase62.encode(cipher) #button == mybase62 encode
				except Exception as e:
					logger.error("An error occurred while encoding with base62: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with base62: " + str(e)
					raise
			
			case 'b64':
				try:
					decoded = mybase64.decode(cipher) #button == base64 decode 
				except Exception as e:
					logger.error("An error occurred while decoding with base64: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with base64: " + str(e)
					raise

			case 'b64e':
				try:
					decoded = mybase64.encode(cipher)#button == base64 encode 
				except Exception as e:
					logger.error("An error occurred while encoding with base64: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with base64: " + str(e)
					raise
			
			case 'rot13':
				try:
					decoded = rot13.rot13(cipher)#button == ROT13 code 
				except Exception as e:
					logger.error("An error occurred while decoding with rot13: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with rot13: " + str(e)
					raise
			
			case 'rot47':
				try:
					decoded = rot47.rot47(cipher) #button == ROT47 code 
				except Exception as e:
					logger.error("An error occurred while decoding with rot47: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with rot47: " + str(e)
					raise
			
			case 'b32':
				try:
					decoded = mybase32.decode(cipher)#button == base32 decode 
				except Exception as e:
					logger.error("An error occurred while decoding with base32: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with base32: " + str(e)
					raise

			case 'b32e':
				try:
					decoded = mybase32.encode(cipher)#button == base32  encode 
				except Exception as e:
					logger.error("An error occurred while encoding with base32: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with base32: " + str(e)
					raise

			case 't2b':
				try:
					decoded = text2binary.encode(cipher)#button == binary code for text 
				except Exception as e:
					logger.error("An error occurred while encoding with text2binary: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with text2binary: " + str(e)
					raise

			case 'b2t' :
				try:
					decoded = binary2text.decode(cipher)#button =text code to binary 
				except Exception as e:
					logger.error("An error occurred while decoding with binary2text: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with binary2text: " + str(e)
					raise

			case "text2XOR2text":
				try:
					decoded = text2XOR2text.encode(cipher,cipher_key)
				except Exception as e:
					logger.error("An error occurred while encoding with text2XOR2text: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with text2XOR2text: " + str(e)
					raise

			case "hex_encode":
				try:
					decoded = hex_encode.encode(cipher)#button == hex encode 
				except Exception as e:
					logger.error("An error occurred while encoding with hex_encode: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with hex_encode: " + str(e)
					raise

			case "hex_decode":
				try:
					decoded = hex_encode.decode(cipher)#button == base64 decode 
				except Exception as e:
					logger.error("An error occurred while decoding with hex_encode: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with hex_encode: " + str(e)
					raise
			
			case "morse_encode":
				try:
					decoded = morse.encode(cipher)#button == Morse encode 
				except Exception as e:
					logger.error("An error occurred while encoding with morse: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with morse: " + str(e)
					raise
			
			case "morse_decode":
				try:
					decoded = morse.decode(cipher)#button == Morse decode 
				except Exception as e:
					logger.error("An error occurred while decoding with morse: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with morse: " + str(e)
					raise
			
			case "atci":
				try:
					decoded = atbash.decatbash(cipher)
				except Exception as e:
					logger.error("An error occurred while decoding with atbash: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with atbash: " + str(e)
					raise
			
			case "vigenere_encode":
				try:
					decoded = vigenere.encode(cipher, cipher_key)#button == Vigenere encode 
				except Exception as e:
					logger.error("An error occurred while encoding with vigenere: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with vigenere: " + str(e)
					raise
			
			case "vigenere_decode":
				try:
					decoded = vigenere.decode(cipher, cipher_key)#button == Vigenere decode
				except Exception as e:
					logger.error("An error occurred while decoding with vigenere: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with vigenere: " + str(e)
					raise
			
			case "octal_encode":
				try:
					decoded = octal.encode(cipher)#button == octal encode
				except Exception as e:
					logger.error("An error occurred while encoding with octal: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with octal: " + str(e)
					raise
			
			case "octal_decode":
				try:
					decoded = octal.decode(cipher)#button == octal decode 
				except Exception as e:
					logger.error("An error occurred while decoding with octal: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with octal: " + str(e)
					raise
			
			case "rot8000_encode":
				try:
					decoded = rot8000.encode(cipher)#button == ROT8000 encode
				except Exception as e:
					logger.error("An error occurred while encoding with rot8000: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with rot8000: " + str(e)
					raise
			
			case "rot8000_decode":
				try:
					decoded = rot8000.decode(cipher)#button == ROT8000 decode
				except Exception as e:
					logger.error("An error occurred while decoding with rot8000: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with rot8000: " + str(e)
					raise
			
			case "base58d":
				try:
					decoded = base58.base58_decode(cipher)#button == base58d decode 
				except Exception as e:
					logger.error("An error occurred while decoding with base58: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with base58: " + str(e)
					raise
			
			case "base58e":
				try:
					decoded = base58.base58_encode(cipher) #button == base58d encode 
				except Exception as e:
					logger.error("An error occurred while encoding with base58: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with base58: " + str(e)
					raise
			
			case "upper":
				try:
					decoded = extra.Upper(cipher)
				except Exception as e:
					logger.error("An error occurred while converting to uppercase: %s", str(e))
					self.ids.string.text = "An error occurred while converting to uppercase: " + str(e)
					raise
			
			case "lower":
				try:
					decoded = extra.Lower(cipher)
				except Exception as e:
					logger.error("An error occurred while converting to lowercase: %s", str(e))
					self.ids.string.text = "An error occurred while converting to lowercase: " + str(e)
					raise
			
			case "reverse":
				try:
					decoded = extra.Reverse(cipher)
				except Exception as e:
					logger.error("An error occurred while reversing: %s", str(e))
					self.ids.string.text = "An error occurred while reversing: " + str(e)
					raise

			case "url_encode":
				try:
					decoded = url.encode(cipher)
				except Exception as e:
					logger.error("An error occurred while encoding with url: %s", str(e))
					self.ids.string.text = "An error occurred while encoding with url: " + str(e)
					raise
			
			case "url_decode":
				try:
					decoded = url.decode(cipher)
				except Exception as e:
					logger.error("An error occurred while decoding with url: %s", str(e))
					self.ids.string.text = "An error occurred while decoding with url: " + str(e)
					raise

			case "leet_encode":
				try:
					decoded = leet.encode(cipher)
				except Exception as e:
					logger.error("An error occurred while encoding with Leet Speak (1337): %s", str(e))
					self.ids.string.text = "An error occurred while encoding with Leet Speak (1337): " + str(e)
					raise
			
			case "leet_decode":
				try:
					decoded = leet.decode(cipher)
				except Exception as e:
					logger.error("An error occurred while decoding with Leet Speak (1337): %s", str(e))
					self.ids.string.text = "An error occurred while decoding with Leet Speak (1337): " + str(e)
					raise
			


		#replace the text in id="string" by the value of the "decoded" variable
		self.ids.string.text = f'{decoded}'
		#after printing the output clear the input field
		self.cipher.text=''
		self.cipher_key.text=''

	def copy(self):
		try:
			c2c.copy(decoded)  # copy to clipboard
		except Exception as e:
			logging.error(f"An error occurred in copy: {e}")
			self.ids.string.text = "Nothing to copy!"
			raise
			

class DcodeKiApp(MDApp):
    def build(self):
        try:
            self.icon = "logo.png"
            sm = ScreenManager()
            sm.add_widget(Builder.load_file("splash.kv"))
            sm.add_widget(DcodLayout(name='main'))
            return sm
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            self.ids.string.text = "An error occurred while loading the file!"
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred in build: {e}")
            self.ids.string.text = "An unexpected error occurred while building the app!"
            raise

class SymbolCipherScreen(Screen):
    pass
class DcodeKiApp(MDApp):
    def build(self):
        self.icon = "logo.png"
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("splash.kv"))
        sm.add_widget(DcodLayout(name='main'))
        sm.add_widget(SymbolCipherScreen(name='symbol_cipher_page'))
        return sm
    def on_start(self):
        try:
            # Schedule the transition to the main screen after 5 seconds
            Clock.schedule_once(self.show_main_screen, 5)
        except Exception as e:
            logging.error(f"An error occurred in on_start: {e}")
            self.ids.string.text = "An error occurred while starting the app!"
            raise

    def show_main_screen(self, dt):
        try:
            sm = self.root
            sm.current = 'main'
        except Exception as e:
            logging.error(f"An error occurred in show_main_screen: {e}")
            self.ids.string.text = "An error occurred while showing the main screen!"
            raise


# If executing this file, then run the program
if __name__ == '__main__':
	DcodeKiApp().run()
