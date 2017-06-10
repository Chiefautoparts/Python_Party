class animal(object):
	def __init__(self, name, health):
		self.name = 'name'
		self.health = health

	def walk(self):
		self.health -= 1
		print self.health
		return self

	def run(self):
		self.health -= 5
		print self.health
		return self

	def display_health(self):
		print "Current health is : " + str(self.health)
		return self
class dog(animal):
	def __init__(self, name,health):
		super(animal,self,'name',health).__init__(name='name',health=150)
		# self.health = 150
	def pet(self):
		self.health += 5
		print self.health
		return self

class dragon(animal):
	def __init__(self,name,health):
		super(animal,self,'name',health).__init__(name='name',health=170)
		self.health = 170
	def fly(self):
		self.health -= 10
		print self.health
		return self
	def display_health(self):
		print str(self.health) + " I AM A DRAGON!!!!"

manBearPig = animal('superCereal', 50000) 

manBearPig.display_health()

boneHead = dog('Loggies')

boneHead.walk().walk().walk().run().run().pet().display_health()


Squeeagle = animal('Squeeagle', 100);

Squeeagle.walk().walk().walk().run().run().display_health()

