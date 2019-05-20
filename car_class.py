from Car import Car

color = input("What color is your car?: ")
year = int(input("Enter the year of your car: "))

# getting information on car brand
boof = False
while (boof != True):
	qbrand = input("a) Ford\nb) Honda\nc) Mercedes-Benz\nWhat brand of car do you have?: ")
	if (qbrand == "a"):
		brand = "Ford"
		boof = True
	elif (qbrand == "b"):
		brand = "Honda"
		boof = True
	elif (qbrand == "c"):
		brand = "Mercedes-Benz\n"
		boof = True
	else:
		print("Invalid input, the accepted inputs are a, b or c. Try again.")

doof = False
while (doof != True):
	qkind = input("a) Sedan\nb) SUV\nc) Sports\nWhat kind of car do you have?: ")
	if (qkind == "a"):
		kind = "Sedan"
		doof = True
	elif (qkind == "b"):
		kind = "SUV"
		doof = True
	elif (qkind == "c"):
		kind = "Sports"
		doof = True
	else:
		print("Invalid input, the accepted inputs are a, b or c. Try again.")






car1 = Car(color, kind, brand, year)

car1.carPrice()


