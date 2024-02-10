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
		err_msg_prefix = 'An error occurred while'
		
		# Dictionary to map method names to corresponding functions and error messages
		method_map = {
			'b45': (mybase45.decode, f'{ err_msg_prefix } decoding with base45: %s'),
			'b45e': (mybase45.encode, f'{ err_msg_prefix } encoding with base45: %s'),
			'b62': (mybase62.decode, f'{ err_msg_prefix } decoding with base62: %s'),
			'b62e': (mybase62.encode, f'{ err_msg_prefix } encoding with base62: %s'),
			'b64': (mybase64.decode, f'{ err_msg_prefix } decoding with base64: %s'),
			'b64e': (mybase64.encode, f'{ err_msg_prefix } encoding with base64: %s'),
			'rot13': (rot13.rot13, f'{ err_msg_prefix } decoding with rot13: %s'),
			'rot47': (rot47.rot47, f'{ err_msg_prefix } decoding with rot47: %s'),
			'b32': (mybase32.decode, f'{ err_msg_prefix } decoding with base32: %s'),
			'b32e': (mybase32.encode, f'{ err_msg_prefix } encoding with base32: %s'),
			't2b': (text2binary.encode, f'{ err_msg_prefix } encoding with text2binary: %s'),
			'b2t': (binary2text.decode, f'{ err_msg_prefix } decoding with binary2text: %s'),
			'text2XOR2text': (text2XOR2text.encode, f'{ err_msg_prefix } encoding with text2XOR2text: %s'),
			'hex_encode': (hex_encode.encode, f'{ err_msg_prefix } encoding with hex_encode: %s'),
			'hex_decode': (hex_encode.decode, f'{ err_msg_prefix } decoding with hex_encode: %s'),
			'morse_encode': (morse.encode, f'{ err_msg_prefix } encoding with morse: %s'),
			'morse_decode': (morse.decode, f'{ err_msg_prefix } decoding with morse: %s'),
			'atci': (atbash.decatbash, f'{ err_msg_prefix } decoding with atbash: %s'),
			'vigenere_encode': (vigenere.encode, f'{ err_msg_prefix } encoding with vigenere: %s'),
			'vigenere_decode': (vigenere.decode, f'{ err_msg_prefix } decoding with vigenere: %s'),
			'octal_encode': (octal.encode, f'{ err_msg_prefix } encoding with octal: %s'),
			'octal_decode': (octal.decode, f'{ err_msg_prefix } decoding with octal: %s'),
			'rot8000_encode': (rot8000.encode, f'{ err_msg_prefix } encoding with rot8000: %s'),
			'rot8000_decode': (rot8000.decode, f'{ err_msg_prefix } decoding with rot8000: %s'),
			'base58d': (base58.base58_decode, f'{ err_msg_prefix } decoding with base58: %s'),
			'base58e': (base58.base58_encode, f'{ err_msg_prefix } encoding with base58: %s'),
			'upper': (extra.Upper, f'{ err_msg_prefix } converting to uppercase: %s'),
			'lower': (extra.Lower, f'{ err_msg_prefix } converting to lowercase: %s'),
			'reverse': (extra.Reverse, f'{ err_msg_prefix } reversing: %s'),
			'url_encode': (url.encode, f'{ err_msg_prefix } encoding with url: %s'),
			'url_decode': (url.decode, f'{ err_msg_prefix } decoding with url: %s'),
			'leet_encode': (leet.encode, f'{ err_msg_prefix } encoding with leet: %s'),
			'leet_decode': (leet.decode, f'{ err_msg_prefix } decoding with leet: %s'),
			'gray_encode': (gray.encode, f'{ err_msg_prefix } encoding with gray: %s'),
			'gray_decode': (gray.decode, f'{ err_msg_prefix } decoding with gray: %s'),
			'ascii_encode': (ascii.encode, f'{ err_msg_prefix } encoding with ascii: %s'),
			'ascii_decode': (ascii.decode, f'{ err_msg_prefix } decoding with ascii: %s'),
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
