from pygame import *
from key_set import *

class game_surface(object):
	def __init__(self, gg):
		self.gg = gg
		self.size = 800, 600
		self.game_screen()
		self.entry_title_s()
		self.game_main_s()
		self.game_key_s()
#		self.game_msg_s()
		self.game_debug_s()
		self.game_sidebar_s()
		self.the_greet_title_s()
		self.the_end_title_s()
	def entry_title_s(self):
		msg_list = ["PyWeek#7 2008-08", 
			"Milker's Solo Entry", 
			"Dominoes String",
			"www.milk2cows.com"]
		self.entry_title_sf = Surface((300, 160))
		n = 10
		for m in msg_list:
			mg = self.gg.gf.bsfont.render(m, 1, (100, 100, 100))
			mgp = mg.get_rect(topleft=(10, n))
			self.entry_title_sf.blit(mg, mgp)
			n += 40
	def the_end_title_s(self):
		msg_list = ["Game is Over.",
			"Thank you for your playing"]
		self.the_end_title_sf = Surface((400, 300))
		n = 10
		for m in msg_list:
			mg = self.gg.gf.bsfont.render(m, 1, (100, 100, 100))
			mgp = mg.get_rect(topleft=(10, n))
			self.the_end_title_sf.blit(mg, mgp)
			n += 40	
	def the_greet_title_s(self):
		msg_list = ["^# Greet !! #^",
			"The game is complete.",
			"Thank you for your playing"]
		self.greet_sf = Surface((400, 300))
		n = 10
		for m in msg_list:
			mg = self.gg.gf.bsfont.render(m, 1, (100, 100, 100))
			mgp = mg.get_rect(topleft=(10, n))
			self.greet_sf.blit(mg, mgp)
			n += 40	
	def game_screen(self):
		self.screen = display.set_mode(self.size)
	def game_main_s(self):
		self.msf = Surface((600,600))
	def game_sidebar_s(self):
		self.logo = self.gg.gi.load_logo()
		self.sidebar_s = Surface((200,600))
		self.sidebar_s.fill((100,0,0))
		self.sidebar_s.blit(self.logo, (100,500))
	def dominoe_block(self, note):
		block_s = Surface((60,120))
		y = 0
		for n in note:
			block_s.blit(self.gg.gi.block_dot[n], (0, y))
			y += 60
		return block_s
	def dominoe_block_line(self, note):
		block_s = Surface((120,60))
		x = 0
		for n in note:
			block_s.blit(self.gg.gi.block_dot[n], (x, 0))
			x += 60
		return block_s
	def game_key_s(self):
		self.key_s = Surface((180, 100))
		self.key_s.fill((100,0,0))
	def game_level_tip_s(self):
		if self.gg.level == 1:
			m = 'a == b'
		elif self.gg.level == 2:
			m = '( a == b + 2 or b == a + 2 )'
		elif self.gg.level == 3:
			m = '( a + b == 5 or a + b == 10 )'
		elif self.gg.level == 4:
			m = '( a == b * 2 or b == a * 2)'
		else:
			m = ''
		mg = self.gg.gf.bsfont.render('Tip: %s' %m, 1, (100, 100, 100))
		mgp = mg.get_rect()
		self.level_tip_s = Surface((500,50))
		self.level_tip_s.fill((0,100,0))
		self.level_tip_s.blit(mg, mgp)
	def game_msg_s(self, t="00:36", c=3, l=2):
		self.msg_s = Surface((180,100))
		self.tm = self.gg.gf.bsfont.render("Time: %s" %t, 1, (100,100,50))
		self.cm = self.gg.gf.bsfont.render("Complete: %i" %c, 1, (100,100,50))
		self.lm = self.gg.gf.bsfont.render("Level: %i" %l, 1, (100,100,50))
		self.tmr = self.tm.get_rect(top=30)
		self.cmr = self.cm.get_rect(top=60)
		self.lmr = self.cm.get_rect(top=0)
		self.msg_s.fill((100,0,0))
		self.msg_s.blit(self.lm, self.lmr)
		self.msg_s.blit(self.tm, self.tmr)
		self.msg_s.blit(self.cm, self.cmr)
	def game_debug_s(self):
		self.debug_s = Surface((180, 100))
		self.debug_s.fill((100,0,0))
