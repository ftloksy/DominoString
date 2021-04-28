from pygame import *

class mouse_c(sprite.Sprite):
	def __init__(self, gg):
		sprite.Sprite.__init__(self)
		self.gg = gg
		self.image = self.gg.gi.load_mouse_a()
		self.rect = self.image.get_rect()
	def update(self):
		self.rect = Rect(
			self.gg.ge.mouse_pos[0]-20, self.gg.ge.mouse_pos[1]-20, 40, 40)
		if self.gg.ge.mouse_state == 1:
			self.image = self.gg.gi.load_mouse_a()
		elif self.gg.ge.mouse_state == -1:
			self.image = self.gg.gi.load_mouse_b()
		elif self.gg.ge.mouse_state == -2:
			self.image = self.gg.gi.load_mouse_c()