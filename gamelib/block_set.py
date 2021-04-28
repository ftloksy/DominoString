from pygame import *
import time as systime

class dominoe_block(sprite.Sprite):
	def __init__(self, gg, b, tl):
		sprite.Sprite.__init__(self)
		self.gg = gg
		self.b = b
		self.image = self.gg.gsf.dominoe_block(self.b)
		self.rect = self.image.get_rect(topleft=tl)
		self.follow_mouse = 0
		self.line_mode = 0
	def update(self):
		if self.rect.collidepoint(self.gg.ge.mouse_pos) and self.gg.ge.mouse_state == -1:
			# for debug.
#			print self.gg.ge.mouse_button
			if self.gg.ge.mouse_button != 1:
				if self.gg.block_last_return_time + 1 < systime.time():
					self.gg.block_last_return_time = systime.time()
					self.gg.gs.sound_turning.play()
					tmp = self.b
					self.b = (tmp[1], tmp[0])
					if self.line_mode == 0:
						self.image = self.gg.gsf.dominoe_block(self.b)
					if self.line_mode == 1:
						self.image = self.gg.gsf.dominoe_block_line(self.b)
			self.follow_mouse = 1
		if self.follow_mouse:
			self.rect = self.image.get_rect(center=self.gg.ge.mouse_pos)
		if self.gg.ge.mouse_state == 1:
			self.follow_mouse = 0
		count = 0
		hit_n = 0
		for c in self.gg.holder_checker:
			if self.rect.collidepoint(c):
				for r in range(4):
					if self.gg.result_list[r] == self.b:
						self.gg.result_list[r] = (-1, -1)
				self.gg.result_list[count] = self.b
				if self.line_mode == 0:
					self.image = self.gg.gsf.dominoe_block_line(self.b)
					self.line_mode = 1
					self.gg.gs.sound_packing.play()
				hit_n += 1
#				debug begin
#				for n in range(4):
#					print self.gg.result_list[n]
#				debug end
			count += 1
		if not hit_n:
			self.image = self.gg.gsf.dominoe_block(self.b)
			self.line_mode = 0