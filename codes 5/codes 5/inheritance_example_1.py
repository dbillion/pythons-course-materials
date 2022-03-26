### parent class
class Bird:
    ''' class documentation'''
    
    def __init__(self):
        self.x = 2
        print("Bird is ready")
    
    def whoisThis(self):
        print("Bird")
    
    def fly(self):
        print("fly faster")

### child class
class Parrot(Bird):
    ''' a child class of the "Bird" class. '''

    def __init__(self):
        # call super() function
        super().__init__()
        print("Parrot is ready")

    def whoisThis(self):
        print("Parrot")

    def sing(self):
        print('singing')



p = Parrot()
##p.whoisThis()
##p.sing()
##p.fly()


# print(isinstance(blu, Parrot))
# print(issubclass(Parrot, Bird))
