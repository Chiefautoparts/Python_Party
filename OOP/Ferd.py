class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = str(mileage)+"mpg"
		self.tax =  if(self.price>10000):
						print self.price * (1.15)
					else:
						print self.price * (1.12)

Ferd = Car(15000, 500, "full", 1)

print Ferd 