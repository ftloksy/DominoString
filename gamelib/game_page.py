from pygame import *
from block_set import *
from key_set import *
from mouse_set import *
import sys, data, time as systime

class game_page(object):
	def __init__(self, gg):
		self.gg = gg
#		self.nloop = 100
	def first_page(self, nloop, title_loop):
		self.mtwoe = self.gg.gf.bfont.render("Milk2Edu", 1, (50, 50, 50))
		self.mtep = self.mtwoe.get_rect(center=(300,300))
#		Play the bg music
		mixer.music.load(data.filepath('game_start.ogg'))
		mixer.music.set_volume(0.8)
		mixer.music.play()
		while nloop + title_loop:
			self.gg.ge.event_checker(event)
			self.gg.gsf.msf.fill((0,0,0))
			if nloop > 0:
				r = int( nloop / 5 )
				if r > 10: r = 10
				nloop -= 1
				self.gg.gsf.msf.blit(self.mtwoe, self.mtep)
				draw.circle(self.gg.gsf.msf, (150,150,150), (300,300), (nloop * 2), r)
			else:
				self.gg.gsf.msf.blit(self.gg.gsf.entry_title_sf, (150, 250))
				title_loop -= 1
			self.gg.gsf.screen.fill((0,0,0))
			self.gg.gsf.screen.blit(self.gg.gsf.msf, (0,0))
			self.gg.gsf.screen.blit(self.gg.gsf.sidebar_s, (600,0))
			display.flip()
#	Now Just for test.
	def block_show_page(self, nloop):
#		Get blocks
		four_b = self.gg.bu.get_me_blocks(28)
		while nloop:
			nloop -= 1
			self.gg.ge.event_checker(event)
			self.gg.gsf.msf.fill((0,100,0))
#			and show it.
			y = 50
			x = 50
			for b in four_b:
				self.gg.gsf.msf.blit(self.gg.gsf.dominoe_block(b), (x,y))
				if x > 400: 
					x = 50
					y += 130
				else:
					x += 65
			self.gg.gsf.screen.fill((0,0,0))
			self.gg.gsf.screen.blit(self.gg.gsf.msf, (0,0))
			self.gg.gsf.screen.blit(self.gg.gsf.sidebar_s, (600,0))
			display.flip()
#	Four block for you
	def four_block_for_you_page(self):
		self.gg.clock.tick(60)
		self.gg.four_b_group.empty()
		self.gg.bu.create_my_blocks(6)
#		four_b = self.gg.bu.get_me_blocks(6)
		while self.gg.time > 0 and self.gg.level < 5:
			self.gg.ge.event_checker(event)
			if int(self.gg.gen_now + 2) > systime.time() :
				self.gg.four_b_group.empty()
				self.gg.bu.create_my_blocks(6)
			self.gg.mouse_hand.update()
			self.gg.key_group.update()
			self.gg.four_b_group.update()
			self.gg.holder_group.update()
			self.gg.gsf.game_level_tip_s()
			self.gg.gsf.msf.fill((0,100,0))
			self.gg.gsf.msf.blit(self.gg.gsf.level_tip_s, (50,5))
#			y = 510
#			x = 50
#			for b in four_b:
#				blk = dominoe_block(self.gg, b, (x, y))
#				self.gg.four_b_group.add(blk)
#				x += 70
#			self.gg.gsf.msf.blit(self.gg.gi.load_string(), (50, 150))
			self.gg.holder_group.draw(self.gg.gsf.msf)
			self.gg.four_b_group.draw(self.gg.gsf.msf)
			
			# Draw All Keys.
			# Handle the msg_sf
			self.gg.time = int(self.gg.start_time + 180 - systime.time() + ((self.gg.level -1) * 120))
			self.gg.gsf.game_msg_s(t='%ss' %self.gg.time, c=self.gg.complete, l=self.gg.level)
#			self.level = 1
#			self.time = "03:00"
#			self.complete = 3
			self.gg.gsf.sidebar_s.blit(self.gg.gsf.msg_s, (20,50))
			self.gg.gsf.sidebar_s.blit(self.gg.gsf.key_s, (20, 400))
##			For debug.
#			if self.gg.ge.mouse_state:
#				if self.gg.ge.mouse_state == 1:
#					m_msg = "UP"
#				elif self.gg.ge.mouse_state == -1:
#					m_msg = "DOWN"
#				elif self.gg.ge.mouse_state == -2:
#					m_msg = "MO"
#				self.gg.gsf.debug_s.fill((100,0,0))
#				self.m_s = self.gg.gf.bsfont.render(
#					'%s: %s,%s' %(m_msg, self.gg.ge.mouse_pos[0], self.gg.ge.mouse_pos[1]),
#					1, (50, 50, 50))
#				self.m_s_p = self.m_s.get_rect()
#				self.gg.gsf.debug_s.blit(self.m_s, self.m_s_p)
#				self.gg.gsf.sidebar_s.blit(self.gg.gsf.debug_s, (20, 200))
			self.gg.gsf.debug_s.fill((100,0,0))
			if self.gg.msg_user_time > systime.time():
#				print 'I am here. %s' %systime.time()
				self.m_s = self.gg.gf.bsfont.render('%s' %self.gg.msg_user, 1, (50, 50, 50))
				self.m_s_p = self.m_s.get_rect()
				self.gg.gsf.debug_s.blit(self.m_s, self.m_s_p)
			self.gg.gsf.sidebar_s.blit(self.gg.gsf.debug_s, (20, 200))
##			Debug End
			self.gg.gsf.screen.fill((0,0,0))
			self.gg.gsf.screen.blit(self.gg.gsf.msf, (0,0))
			self.gg.gsf.screen.blit(self.gg.gsf.sidebar_s, (600,0))
			self.gg.key_group.draw(self.gg.gsf.screen)
			self.gg.mouse_group.draw(self.gg.gsf.screen)
			display.flip()
			
	def complete_page(self, nloop, title_loop, sf):
#		self.gg.gsf.the_end_title_s()
		self.mtwoe = self.gg.gf.bfont.render("Milk2Edu", 1, (50, 50, 50))
		self.mtep = self.mtwoe.get_rect(center=(300,300))
#		Play the bg music
		mixer.music.load(data.filepath('game_start.ogg'))
		mixer.music.set_volume(0.8)
		mixer.music.play()
		while nloop + title_loop:
			self.gg.ge.event_checker(event)
			self.gg.gsf.msf.fill((0,0,0))
			if title_loop > 0:
				self.gg.gsf.msf.blit(sf, (150, 250))
				title_loop -= 1
			else:
				r = int( nloop / 5 )
				if r > 10: r = 10
				nloop -= 1
				self.gg.gsf.msf.blit(self.mtwoe, self.mtep)
				draw.circle(self.gg.gsf.msf, (150,150,150), (300,300), (nloop * 2), r)
			self.gg.gsf.screen.fill((0,0,0))
			self.gg.gsf.screen.blit(self.gg.gsf.msf, (0,0))
			self.gg.gsf.screen.blit(self.gg.gsf.sidebar_s, (600,0))
			display.flip()