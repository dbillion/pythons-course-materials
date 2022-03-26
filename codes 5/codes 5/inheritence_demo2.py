class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id
    
    def disp(self):
        print(self.name)
        print(self.age)
        print(self.emp_id)


####
e = Employee('Tom', 25, 12312)
e.disp()

