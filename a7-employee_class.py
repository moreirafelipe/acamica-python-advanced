import typed

class Employee(object):
    name = typed.string("name")
    age = type.Integer("age")
    salary = typed.Float("salary")

    #Define constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary