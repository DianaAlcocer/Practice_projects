class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        name = f'{self.year} {self.make} {self.model}'
        return name.title()

    def read_odometer(self):
        print(f'Este auto tiene {self.odometer_reading} millas')

    def update_odometer(self,miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print('¡No puedes hacer retroceder un odometro!')

    def increase_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print('No puedes hacer retroceder un odometro!')

#my_new_car = Car('audi','a4',2024,)
my_used_car = Car('subaru','interior',2019)

#print(my_new_car.get_descriptive_name())
print(my_used_car.get_descriptive_name())

my_used_car.read_odometer()

#my_new_car.update_odometer(23)
my_used_car.update_odometer(23_500)

#my_new_car.read_odometer()
my_used_car.read_odometer()

my_used_car.increase_odometer(100)

my_used_car.read_odometer()

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery_size = 40

    def describe_battery(self):
        print(f'This car has a battery size of {self.battery_size}')

my_leaf = ElectricCar('nissan','lead',2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
