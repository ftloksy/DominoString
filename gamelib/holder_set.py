from pygame import *

class holder_set(sprite.Sprite):
	def __init__(self, gg, c):
		sprite.Sprite.__init__(self)
		self.gg = gg
		self.mouse_over = 0
		self.image = self.gg.gi.load_holder_a()
		self.rect = self.image.get_rect(center=c)
	def update(self):
		if self.rect.collidepoint(self.gg.ge.mouse_pos):
			self.mouse_over = 1
		else:
			self.mouse_over = 0
		if self.mouse_over == 0:
			self.image = self.gg.gi.load_holder_a()
		else:
			self.image = self.gg.gi.load_holder_b()