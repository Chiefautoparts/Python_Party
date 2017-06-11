class MathDojo(object):
	def __init__(self,a,b):
		self.a = a
		self.b = b
		self.sum = sum
		self.sub = 'sub' 
	def add(self,a):
		self.sum = a+b
		print self.sum
		return self

	def subtract(self,a):
		self.sub = a-b
		print self.sub
		return self




math = MathDojo()

math.subtract(1,2)