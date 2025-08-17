class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f'First name: {self.first_name} \nLast name: {self.last_name}')

    def greet_user(self):
       print(f'Bienvenido {self.first_name} {self.last_name}')

    def read_login_attempts(self):
        print(f'Login attempts: {self.login_attempts}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = User('John','Doe')
user_1.describe_user()
user_1.greet_user()
user_1.read_login_attempts()
user_1.increment_login_attempts()
user_1.read_login_attempts()
user_1.increment_login_attempts()
user_1.read_login_attempts()
user_1.increment_login_attempts()
user_1.read_login_attempts()
user_1.reset_login_attempts()
user_1.read_login_attempts()

user_2 = User('Juan','Perez')
user_2.describe_user()
user_2.greet_user()