class Car:
	
	def __init__(self, color, kind, brand, year):
		self.color = color
		self.kind = kind
		self.brand = brand
		self.year = year

	def whatCar(self):
		print("This car is a " + self.color + " " + self.year + " " + self.brand + ".")

	
	def carPrice(self):
		if (self.brand == "Mercedes-Benz"):
			price = 50000
		elif (self.brand == "Honda"):
			price = 25000
		elif self.brand == "Ford":
			price = 12500

		if (self.year <= 1990):
			price += 500
		elif (self.year <= 2010):
			price += 1500
		elif (self.year > 2010):
			price += 4500

		if (self.kind == "Sedan"):
			price += 1000
		elif (self.kind == "Sports"):
			price += 2000
		elif (self.kind == "SUV"):
			price += 3000

		print("The price of the car is $", price, " dollars." )






	