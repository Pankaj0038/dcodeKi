#!/usr/bin/python3

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock

from encoders import rot47, rot13, mybase64, mybase32,extra, text2XOR2text, hex_encode, binary2text, text2binary, morse, atbash, octal, rot8000, vigenere, base58, mybase45, mybase62, url, leet, gray, ascii
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
	def press(self, method):
		global decoded

		#on button press store the input field in cipher object
		cipher = self.cipher.text
		cipher_key = self.cipher_key.text
		
		# Dictionary to map method names to corresponding functions and error messages
		method_map = {
			'b45': (mybase45.decode, 'An error occurred while decoding with base45: %s'),
			'b45e': (mybase45.encode, 'An error occurred while encoding with base45: %s'),
			'b62': (mybase62.decode, 'An error occurred while decoding with base62: %s'),
			'b62e': (mybase62.encode, 'An error occurred while encoding with base62: %s'),
			'b64': (mybase64.decode, 'An error occurred while decoding with base64: %s'),
			'b64e': (mybase64.encode, 'An error occurred while encoding with base64: %s'),
			'rot13': (rot13.rot13, 'An error occurred while decoding with rot13: %s'),
			'rot47': (rot47.rot47, 'An error occurred while decoding with rot47: %s'),
			'b32': (mybase32.decode, 'An error occurred while decoding with base32: %s'),
			'b32e': (mybase32.encode, 'An error occurred while encoding with base32: %s'),
			't2b': (text2binary.encode, 'An error occurred while encoding with text2binary: %s'),
			'b2t': (binary2text.decode, 'An error occurred while decoding with binary2text: %s'),
			'text2XOR2text': (text2XOR2text.encode, 'An error occurred while encoding with text2XOR2text: %s'),
			'hex_encode': (hex_encode.encode, 'An error occurred while encoding with hex_encode: %s'),
			'hex_decode': (hex_encode.decode, 'An error occurred while decoding with hex_encode: %s'),
			'morse_encode': (morse.encode, 'An error occurred while encoding with morse: %s'),
			'morse_decode': (morse.decode, 'An error occurred while decoding with morse: %s'),
			'atci': (atbash.decatbash, 'An error occurred while decoding with atbash: %s'),
			'vigenere_encode': (vigenere.encode, 'An error occurred while encoding with vigenere: %s'),
			'vigenere_decode': (vigenere.decode, 'An error occurred while decoding with vigenere: %s'),
			'octal_encode': (octal.encode, 'An error occurred while encoding with octal: %s'),
			'octal_decode': (octal.decode, 'An error occurred while decoding with octal: %s'),
			'rot8000_encode': (rot8000.encode, 'An error occurred while encoding with rot8000: %s'),
			'rot8000_decode': (rot8000.decode, 'An error occurred while decoding with rot8000: %s'),
			'base58d': (base58.base58_decode, 'An error occurred while decoding with base58: %s'),
			'base58e': (base58.base58_encode, 'An error occurred while encoding with base58: %s'),
			'upper': (extra.Upper, 'An error occurred while converting to uppercase: %s'),
			'lower': (extra.Lower, 'An error occurred while converting to lowercase: %s'),
			'reverse': (extra.Reverse, 'An error occurred while reversing: %s'),
			'url_encode': (url.encode, 'An error occurred while encoding with url: %s'),
			'url_decode': (url.decode, 'An error occurred while decoding with url: %s'),
			'leet_encode': (leet.encode, 'An error occurred while encoding with leet: %s'),
			'leet_decode': (leet.decode, 'An error occurred while decoding with leet: %s'),
			'gray_encode': (gray.encode, 'An error occurred while encoding with gray: %s'),
			'gray_decode': (gray.decode, 'An error occurred while decoding with gray: %s'),
			'ascii_encode': (ascii.encode, 'An error occurred while encoding with ascii: %s'),
			'ascii_decode': (ascii.decode, 'An error occurred while decoding with ascii: %s'),
		}
		
		# Call the corresponding function based on the method
		try:
			function, error_message = method_map[method]
			decoded = function(cipher, cipher_key) if method in {'text2XOR2text', 'vigenere_encode', 'vigenere_decode'} else function(cipher)
		except Exception as e:
			logger.error(error_message % str(e))
			self.ids.string.text = error_message % str(e)
			raise
		
		# Replace the text in id="string" by the value of the "decoded" variable
		self.ids.string.text = f'{decoded}'
		# After printing the output, clear the input field
		self.cipher.text = ''
		self.cipher_key.text = ''

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
