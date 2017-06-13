class call(object):
	def __init__(self, Idnum, name, phoneNum, time, reason):
		self.Idnum = Idnum
		self.name = 'name'
		self.phoneNum = phoneNum
		self.time = time
		self.reason = 'reason'

	def display(self):
		print self.Idnum,self.name,self.phoneNum,self.time,self.reason
		return self

class callCenter(object):
	def __init__(self, call, queue_size):
		self.call = call
		self.queue.size = 