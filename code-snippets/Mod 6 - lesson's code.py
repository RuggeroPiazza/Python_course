#########FUNCTIONS VS METHODS##############

# standalone
def say_hello():
	print("hello")

# associated with objects
my_list = []
my_list.append(1)


# invocation
say_hello() # by name
my_list.append(1)


# functions can be organised in modules or standalone entitites
# methods are organised within classes




###############OOP PRINCIPLES################

# why? to mimic real-world objects

# real life things has attributes. ex cars (brand, color, year, model)
# a class is an "object factory": it allows us to create objects

# how to create an instance (object)
class Car:
    pass

print(Car())

car_1 = Car()
car_2 = Car()

# assigning attributes directly to the object
car_1.brand = "Ford"
car_2.brand = "Honda"

print(car_1.brand)


# creating a class and assigning attributes using the constructor
class Car:
    # class variable
    current_year = 2023
    num_of_cars = 0
    def __init__(self, brand, color, year, model):
        self.brand = brand
        self.color = color
        self.year = year
        self.model = model
        Car.num_of_cars += 1

    def ignition(self):
        print(f"The {self.model} is on")

    def drive(self):
        print("driving...")

    def stop(self):
        print("car stopped")

    def turn_off(self):
        print("Car is off")

    def age(self):
        print(self.current_year - int(self.year))

    # altering the str() behaviour
    def __str__(self):
        return f"The {self.model} is a {self.brand}"


car_1 = Car("Ford", "grey", "1986", "escort")

print(car_1.brand)
print(car_1.color)
print(car_1.year)
print(car_1.model)

car_1.ignition()
car_1.drive()
car_1.stop()
car_1.off()

print(Car.ignition(car_1))


print(car_1.current_year) # check if the attribute exist in the instance first, and then in the class
print(Car.current_year)

# we can use __dict__ to show all the attributes associated

print(car_1.__dict__)
print(Car.__dict__)

# I can set the attributes to the instance itself, a different one
car_1.current_year = 1992
print(car_1.__dict__)

car_2 = Car("Fiat", "white", "2006", "500")
car_1.age()
print(car_1.__dict__)
car_2.age()
print(car_2.__dict__)


# example of a class variable that don't use self

print(Car.num_of_cars)
print(car_1.num_of_cars)




############# DUNDER METHODS #######################
# comment out the function at line 74 and see the difference
# in the output of the following print statement
print(str(car_1))
