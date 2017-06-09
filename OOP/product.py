class products(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = self.add_tax
		self.status = "for sale"
	def sell(self):
		self.status = "sold"
		print self.status
		return self
<<<<<<< HEAD
	def add_tax():
	def Return():
	def display():
=======
	def add_tax(self):
		# self.cost * (1.12)
		print "Cost after tax is " + self.cost*(1.12)
		return self
	'''def returned():

	def display():'''
bike = products(50, "party bike", 3, "awesome")

bike.add_tax()
>>>>>>> 411fb2933cb594e754788f00c1408df38290fae4
