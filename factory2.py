# Factory Classes

class Vehicle(object):
	def __init__(self, make, model, color, year):
		self.make = make
		self.model = model
		self.color = color
		self.year = year

class CarVehicle(Vehicle):
	def __init__(self, make, model, color, year):
		super(CarVehicle, self).__init__(make, model, color, year)
	def drive(self):
		print 'The ' + self.color + 'car is drivable!'
		
class TankVehicle(Vehicle):
	def __init__(self, make, model, color, year):
		super(TankVehicle, self).__init__(make, model, color, year)
	def shoot(self):
		print 'The ' + self.color + ' tank is now able to shoot!'

class Factory():
	def createVehicle(self, vehicleType):
		make = raw_input('Enter your vehicles make. ')
		model = raw_input('Enter your vehicle model. ')
		color = raw_input('Enter your vehicles color. ')
		year = raw_input('Enter your vehicles year. ')
		if vehicleType == 'Car':
			return CarVehicle(make, model, color, year)
		elif vehicleType == 'Tank':
			return TankVehicle(make, model, color, year)

			
our_factory = Factory()
my_car = our_factory.createVehicle('Car')
my_tank = our_factory.createVehicle('Tank')
my_car.drive()
my_tank.shoot()

