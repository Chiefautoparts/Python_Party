class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = str(mileage)+"mpg"
		if self.price>10000:
			self.tax = (self.price * (1.15))
		else:
			self.tax = (self.price * (1.12))
		self.display_all = display_all()
			return self.price,self.speed,self.fuel,self.mileage,self.tax
			return self	


megaFerd = Car(15000, 500, "full", 1)
halfFerd = Car(9000, 120, "almost full", 22)
doubleFerdly = Car(100000, 320, "fullish", 86)
fakeCar = Car(8500, 160, "half full", 30)
littleBigBear = Car(10, 25, "on fumes", 10)
realCar = Car(9500, 120, "overfilled", 15)

display.all