import os
import glob
# from datetime import timedelta
from mutagen.mp3 import MP3

class InvoiceFiles:
	def __init__(self):
		self.home_directory = 'C:\\Users\\User\\Downloads'
		self.audio_information = {}
	def get_directory(self):
		if self.home_directory == '':
			return 'Home directory is empty!'
		return self.home_directory
	def print_audio_information(self):
		for item in self.audio_information:
			print('Name :: {} [===] Value :: {}'.format(item, self.audio_information[item]))
	def gather_audio(self):
		audio_files = [ f for f in glob.glob(self.home_directory + '\\*.mp3') ]
		for f in audio_files:
			audio = MP3(f)
			# self.audio_information[f] = str(timedelta(seconds=audio.info.length)) 
			self.audio_information[f] = audio.info.length
		print("-> Files for this week:")
		self.print_audio_information()
	def get_audio_information(self):
		if len(self.audio_information) == 0:
			print('Audio information is empty!')
			print('Gathering files...')
			self.gather_audio()
		return self.audio_information
