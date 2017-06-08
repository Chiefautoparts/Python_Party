class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.name = self
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = str(mileage)+"mpg"
		if self.price>10000:
			self.tax = "0.15"
		else:
			self.tax = "0.12"
 
	def display_all(self):
		print " "	
		print "Price: " + str(self.price)
		print "Speed: " + str(self.speed)
		print "Fuel: " + str(self.fuel)
		print "Mileage: " + str(self.mileage)
		print "Tax: " + str(self.tax)
		



megaFerd = Car(15000, 500, "full", 1)
halfFerd = Car(9000, 120, "almost full", 22)
doubleFerdly = Car(100000, 320, "fullish", 86)
fakeCar = Car(8500, 160, "half full", 30)
littleBigBear = Car(10, 25, "on fumes", 10)
realCar = Car(9500, 120, "overfilled", 15)

megaFerd.display_all()
halfFerd.display_all()
doubleFerdly.display_all()
fakeCar.display_all()
littleBigBear.display_all()
realCar.display_all()