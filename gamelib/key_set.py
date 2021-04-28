from pygame import *
import time as systime

#class stop_key(sprite.Sprite):
#	def __init__(self, gg, lt=(620,450)):
#		sprite.Sprite.__init__(self)
#		self.gg = gg
#		self.image = self.gg.gi.load_stop()
#		self.rect = self.image.get_rect(topleft=lt)
#	def update(self):
#		if self.rect.collidepoint(self.gg.ge.mouse_pos) and self.gg.ge.mouse_state == -1 and self.gg.ge.mouse_button == 1:
#			self.gg.gen = 0 

class reg_key(sprite.Sprite):
	def __init__(self, gg, lt=(620,400)):
		sprite.Sprite.__init__(self)
		self.gg = gg
		self.image = self.gg.gi.load_regenerate()
		self.rect = self.image.get_rect(topleft=lt)
#		self.regenerate = 0 
	def update(self):
		if self.rect.collidepoint(self.gg.ge.mouse_pos) and self.gg.ge.mouse_state == -1 and self.gg.ge.mouse_button == 1:
#			self.gg.gen = 1
			self.gg.gs.sound_genning.play()
			self.gg.gen_now = systime.time()
			#self.gg.complete_state = 0

class commit_key(sprite.Sprite):
	def __init__(self, gg, lt=(620, 350)):
		sprite.Sprite.__init__(self)
		self.gg = gg
		self.image = self.gg.gi.load_commit()
		self.rect = self.image.get_rect(topleft=lt)
#		self.commit = 0
	def update(self):
		if self.rect.collidepoint(self.gg.ge.mouse_pos) and self.gg.ge.mouse_state == -1 and self.gg.ge.mouse_button == 1:
			self.gg.commit = 1
			self.gg.gs.sound_commit.play()
		else:
			self.gg.commit = 0
		if self.gg.commit:
#			check self.gg.result_list
#			print 'Commit'
			self.gg.gc.check()
			if self.gg.gc.get_result():
#				print 'Success'
				self.gg.last_complete_list = self.gg.result_list
				if self.gg.last_complete_time + 2 < systime.time():
					
					self.gg.complete += 1
					self.gg.last_complete_time = systime.time()
					
					if self.gg.complete and ( self.gg.complete == self.gg.complete / 3 * 3 ):
						if self.gg.last_add_level_complete < self.gg.complete:
							self.gg.gs.sound_levelup.play()
							self.gg.level += 1
							self.gg.last_add_level_complete = self.gg.complete
							self.gg.msg_user = 'Level Up'
							self.gg.msg_user_time = systime.time() + 2
					else:
						self.gg.gs.sound_success.play()
					
				self.gg.msg_user = "pass."
				self.gg.msg_user_time = systime.time() + 2
				self.gg.gen_now = systime.time()
			else:
				if self.gg.msg_user != 'Level Up': self.gg.msg_user = "UnPass !"
				self.gg.msg_user_time = systime.time() + 2
