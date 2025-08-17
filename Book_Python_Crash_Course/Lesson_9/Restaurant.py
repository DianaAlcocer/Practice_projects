class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name,self.cuisine_type)

    def open_restaurant(self):
        print('The restaurant is open')

    def read_number_served(self):
        print(f'Clientes atendidos: {self.number_served}')

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self,number):
        self.number_served += number

restaurant_1 = Restaurant('Mariscos','Mediterranean cuisine')
restaurant_2 = Restaurant('Tacos del Barrio','Mexican cuisine')
restaurant_3 = Restaurant('Pizzerola','Italian cuisine')

print(restaurant_1.restaurant_name)
print(restaurant_1.cuisine_type)

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_1.read_number_served()
restaurant_1.number_served = 2
restaurant_1.read_number_served()
restaurant_1.set_number_served(3)
restaurant_1.increment_number_served(7)
restaurant_1.read_number_served()

restaurant_2.describe_restaurant()
restaurant_2.read_number_served()

restaurant_3.describe_restaurant()
restaurant_3.read_number_served()

