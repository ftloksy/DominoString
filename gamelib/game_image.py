from pygame import *
import data

class game_image(object):
	def __init__(self, gg):
		self.gg = gg
		self.block_dot = [self.load_zero(),
			self.load_one(),
			self.load_two(),
			self.load_three(),
			self.load_four(),
			self.load_five(),
			self.load_six()]
	def load_logo(self): return image.load(data.load("M_E2.png"))
	def load_zero(self): return image.load(data.load("0.png"))
	def load_one(self): return image.load(data.load("1.png"))
	def load_two(self): return image.load(data.load("2.png"))
	def load_three(self): return image.load(data.load("3.png"))
	def load_four(self): return image.load(data.load("4.png"))
	def load_five(self): return image.load(data.load("5.png"))
	def load_six(self): return image.load(data.load("6.png"))
	def load_regenerate(self): return image.load(data.load("regenerate.png"))
	def load_stop(self): return image.load(data.load("stop.png"))
	def load_string(self): return image.load(data.load("string.png"))
	def load_mouse_a(self): return image.load(data.load("mouse1.png"))
	def load_mouse_b(self): return image.load(data.load("mouse2.png"))
	def load_mouse_c(self): return image.load(data.load("mouse3.png"))
	def load_holder_a(self): return image.load(data.load("block_holder1.png"))
	def load_holder_b(self): return image.load(data.load("block_holder2.png"))
	def load_commit(self): return image.load(data.load("commit.png"))