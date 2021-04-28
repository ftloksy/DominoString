from pygame import *
import sys

class game_event(object):
	def __init__(self, gg):
		self.gg = gg
		self.mouse_state = 0
		self.mouse_pos = (0,0)
	def event_checker(self, event):
		self.e_list = event.get()
		for e in self.e_list:
			if e.type == QUIT: sys.exit()
			if e.type == MOUSEBUTTONUP: 
				self.mouse_state = 1
				self.mouse_pos = e.pos
			if e.type == MOUSEBUTTONDOWN: 
				self.mouse_state = -1
				self.mouse_pos = e.pos
				self.mouse_button = e.button
			if e.type == MOUSEMOTION:
				self.mouse_state = -2
				self.mouse_pos = e.pos