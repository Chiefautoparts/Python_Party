
class Bike(object):
	def __init__(self, price, max_speed):
		self.price = '$' + str(price)
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		if self.miles<0:#checks if the miles are positive, if negative mileage will only show zero
			self.miles = 0
		print self.price,self.max_speed,self.miles
		return self
	def ride(self):
		self.miles+=10
		print "Riding" + " Total miles now at " + str(self.miles)
		return self
	def reverse(self):
		self.miles-=5
		if self.miles>=0:
			print "Reversing" + " Total miles now at " + str(self.miles)
		else:
			print "Reversing"
		return self

Sunday = Bike(450, '22mph')
Stolen = Bike(475, '20mph')
FBM = Bike(550, '65mph')

# Sunday.displayInfo()
# Sunday.ride()
# Sunday.reverse()

Sunday.ride().ride().ride().displayInfo()

Stolen.ride().ride().reverse().reverse().displayInfo()

FBM.reverse().reverse().reverse().displayInfo()