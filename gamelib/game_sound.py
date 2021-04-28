# In this file just handle the sound eff.
from pygame import *
import data

class game_sound(object):
	def __init__(self, gg):
		self.gg = gg
		self.sound_packing = self.load_pack()
		self.sound_turning = self.load_turn()
		self.sound_genning = self.load_gen()
		self.sound_commit = self.load_commit()
		self.sound_success = self.load_success()
		self.sound_levelup = self.load_levelup()
	def load_pack(self): return mixer.Sound(data.filepath('packing.ogg'))
	def load_turn(self): return mixer.Sound(data.filepath("turning.ogg"))
	def load_gen(self): return mixer.Sound(data.filepath("genning.ogg"))
	def load_commit(self): return mixer.Sound(data.filepath("submit.ogg"))
	def load_success(self): return mixer.Sound(data.filepath("success.ogg"))
	def load_levelup(self): return mixer.Sound(data.filepath("levelup.ogg"))