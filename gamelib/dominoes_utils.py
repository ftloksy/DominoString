import random, sys
from block_set import * 

class dominoes_utils(object):
	def __init__(self, gg, n):
		self.gg = gg
		self.n = n + 1
		self.create_blocks()
	def create_blocks(self):
		self.blocks = []
		for a in range(self.n):
			for b in range(a + 1):
				block = [a, b]
				self.blocks.append(block)
#		return blocks
	def get_me_blocks(self, n):
		if n > len(self.blocks):
			print "You need something bigger then system."
			sys.exit()
		else:
			return random.sample(self.blocks, n)
	def create_my_blocks(self, n):
		four_b = self.get_me_blocks(n)
		y = 450
		x = 50
		for b in four_b:
			blk = dominoe_block(self.gg, b, (x, y))
			self.gg.four_b_group.add(blk)
			x += 70
#		self.gg.four_b_group.draw(self.gg.gsf.msf)

if __name__ == "__main__":
	d = dominoes_utils(6)
	ds = d.get_me_blocks(4)
	print ds	