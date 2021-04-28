from pygame import *
import data

class game_font(object):
	def __init__(self, gg):
		self.gg = gg
		self.base_font()
	def base_font(self):
		self.bfont = font.Font(None, 56)
		self.bsfont = font.Font(None, 36)