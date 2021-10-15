# How to use classes

class people:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    boss = ('Jesus', 'chitty', 36)
    x = 21

print(people.boss)

oli = people('Olivia', 'Lopez Alaniz', 25)
jesus = people('Jesus', 'chitty', 36)

print(oli.age)
print(jesus.name)

# Setting a variable inside a class (tatic) is not the same as an instance level variable
print(people.boss == jesus)

print(people.x)
