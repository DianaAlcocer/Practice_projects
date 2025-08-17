class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} ahora esta sentado')

    def roll_over(self):
        print(f'{self.name} volteado!')

mi_perro = Dog('Willie',6)
tu_perro = Dog('Lucy',3)

print(f'\nEl nombre de mi perro es {mi_perro.name}.')
print(f'Mi perro tiene {mi_perro.age} años.')
mi_perro.sit()
mi_perro.roll_over()

print(f'\nEl nombre de mi perro es {tu_perro.name}.')
print(f'Mi perro tiene {tu_perro.age} años.')
tu_perro.sit()
tu_perro.roll_over()
