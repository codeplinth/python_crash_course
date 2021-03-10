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

my_new_car = Car('audi','a4',2021)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(2700)
my_new_car.read_odometer()

my_used_car = Car('subaru','outback',2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

