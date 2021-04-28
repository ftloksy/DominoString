from pygame import *
from key_set import *
from mouse_set import *
from holder_set import *
import game_page, game_surface, game_image, check_result
import game_font, game_event, game_sound
import dominoes_utils
import time as systime

# This class is define the game_object's namespace.
class game_global(object):
	def __init__(self):
		init()
		mouse.set_visible(0)
		
		self.gi = game_image.game_image(self)
		self.gs = game_sound.game_sound(self)
#		self.sound_packing = self.gs.load_pack()
		self.gen = 0
		self.commit = 0
		self.level = 1
		self.start_time = systime.time()
		self.time = int(self.start_time + 180 - systime.time() + ((self.level -1) * 120))
		self.complete = 0
		self.last_complete_time = systime.time()
		self.block_last_return_time = systime.time()
		self.last_add_level_complete = 0
		self.gen_now = systime.time()
		self.msg_user = "Welcome !"
		self.msg_user_time = systime.time() + 5
#		self.last_complete_list = {}
		self.holder_checker = [(75,200), (225,200), (375,200), (525,200)]
		self.result_list = { 0: (-1,-1), 1: (-1,-1), 2: (-1,-1), 3: (-1,-1)}
		self.holder_group = sprite.Group()
		for c in self.holder_checker:
			h = holder_set(self, c)
			self.holder_group.add(h)
			
		#		set the keys.
#		self.stop_key = stop_key(self)
		self.reg_key = reg_key(self)
		self.commit_key = commit_key(self)
		self.key_group = sprite.Group()
#		self.key_group.add(self.stop_key)
		self.key_group.add(self.reg_key)
		self.key_group.add(self.commit_key)
		# Set the four_b group.
#		four_b = self.gg.bu.get_me_blocks(6)
		self.four_b_group = sprite.Group()
		# Set the mouse.
		self.mouse_group = sprite.Group()
		self.mouse_hand = mouse_c(self)
		self.mouse_group.add(self.mouse_hand)
		# Setting end.
		
		self.clock = time.Clock()
		self.gf = game_font.game_font(self)

		self.gsf = game_surface.game_surface(self)
		self.gp = game_page.game_page(self)
		self.ge = game_event.game_event(self)
		self.gc = check_result.check_result(self)
#		On now Just handle double six
		self.bu = dominoes_utils.dominoes_utils(self, 6)
