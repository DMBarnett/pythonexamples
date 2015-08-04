
# with year, make, model and color

class FactoryVehicle():
	def __init__(self, key, next):
		self.key = key
		self.next = next



class FactoryOutput():
	def __init__(self):
		self.head = None
	def add(self, key):
		self.head = FactoryVehicle(key, self.head)
	def remove(self, key):
		current = self.head
		while current.next != None:
			if curent.key == key:
				current.key = current.next.key
				current.next = current.next.next
				return None
			elif current.next.key == key:
				if current.next.next == None:
					current.next = None
					return None
				else:
					current = current.next
			else:
				current = current.next
	def printVehicle(self):
		current = self.head
		if current == None:
			print 'You haven\'t chosen anything yet!'
		else:
			print 'Your new vehicle is a',
			while current.next != None:
				print current.key,
				current = current.next
			print current.key,
			print '!'
			

#create array outside of the class, then use class to build it?

my_new_vehicle = FactoryOutput()
		
my_new_vehicle.add(raw_input('Would you like to buy a Ford, a Boeing, an Abrams, or a Mastercraft?'))
my_new_vehicle.add(raw_input('What color would you like it to be?'))
my_new_vehicle.add(raw_input('And what year?'))


my_new_vehicle.printVehicle()

	
		
