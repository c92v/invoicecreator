import os
import glob
import re
from shutil import move
from datetime import date, timedelta
from mutagen.mp3 import MP3

class InvoiceFiles:
	def __init__(self, directory):
		self.home_directory = directory
		self.date = date.today().isoformat()
		self.audio_information = {}
	def get_directory(self):
		if self.home_directory == '':
			return 'Home directory is empty!'
		return self.home_directory
	def get_date(self):
		return self.date
	def get_audio_information(self):
		for item in self.audio_information:
			print('Name - {} ; Value - {}'.format(item, self.audio_information[item]))
	def gather_audio(self):
		audio_files = [ f for f in glob.glob(self.home_directory + '\\*.mp3') ]
		for f in audio_files:
			audio = MP3(f)
			self.audio_information[f] = str(timedelta(seconds=audio.info.length)) 
			self.get_audio_information()

