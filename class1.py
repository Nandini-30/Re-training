
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def description(self):
        print(f"This is a {self.make} {self.model} made in {self.year}.")

my_car = Car("Audi", "Sedan", 2020)
print(my_car.make)  
print(my_car.model)
print(my_car.year)

my_car.description() 
