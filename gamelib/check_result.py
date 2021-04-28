class check_result(object):
	def __init__(self, gg):
		self.gg = gg
	def check(self):
		d = self.gg.result_list
		self.check_list = (
			(d[0][1], d[1][0]), 
			(d[1][1], d[2][0]),
			(d[2][1], d[3][0]))
		for c in self.check_list:
			if c[0] >= 0 and c[1] >= 0 and self.level(c[0], c[1], self.gg.level):
				self.result = 1
			else:
				self.result = 0
	def get_result(self):
		return self.result
	def level(self, a, b, l):
		if l == 1 and a == b:
			return 1
		elif l == 2 and ( a == b + 2 or b == a + 2 ):  
			return 1
		elif l == 3 and ( a + b == 5 or a + b == 10 ):
			return 1
		elif l == 4 and ( a == b * 2 or b == a * 2):
			return 1
		else:
			return 0