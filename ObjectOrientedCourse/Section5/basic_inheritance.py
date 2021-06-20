# Example

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, {self.name.title()}.'


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.id = employee_id


p_1 = Person('name_1')
p_2 = Person('name_2')

print(p_1.greet())
print(p_2.greet())

e_1 = Employee('name_3', 1)
e_2 = Employee('name_4', 2)

print(e_1.greet())
print(e_2.greet())
