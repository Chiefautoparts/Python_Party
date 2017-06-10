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
	def __init__(self):
		super(animal,self).__init__()
		self.health = 150
	def pet(self):
		self.health += 5
		print self.health
		return self



boneHead = dog()

boneHead.walk().walk().walk().run().run().pet().display_health()

# Squeeagle = animal()

# Squeeagle = animal('Squeeagle', 100);

# Squeeagle.walk().walk().walk().run().run().display_health()

