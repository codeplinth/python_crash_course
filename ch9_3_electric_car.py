#Inheritance
class Car:
    """A simple attempt to model a Car"""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a Car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted description"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Show the cars mileage"""
        print(f"The car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        """
        Set odometer reading to a given value
        Reject the change if it attempts to set the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer")

    def increment_odometer(self,miles):
        """Add given miles to odometer reading"""            
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Simulate filling up of the gas tank"""
        print(f"Gas tank is now full !!")


class ElectricCar(Car):
    """Represent aspects of a car specific to electric cars"""

    def __init__(self,make,model,year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make,model,year)
        self.battery_size = 75
    
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has {self.battery_size}-kWh battery")

    def fill_gas_tank(self):
        """Ëlectric cars do not need a gas tank"""
        print("This car does not need a gas tank")

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()