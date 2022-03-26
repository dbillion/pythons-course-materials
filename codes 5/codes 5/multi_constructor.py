class Bird:
    ''' A simple class example '''
    
    # instance attributes
    def __init__(self):
        self.name = 'parrot'
        self. age = 3
        print('no arugument constructor is called')
	
	
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('two argument constructor is called')
		
	
    def __init__(self, n = 'blue', a = 1, b = 24):
        self.name = n
        self.age = a
        self.feathers = b
        print('default values constructor is called')
		
		
    # instance method
    def getname(self):
        return "{} is my pet's name".format(self.name)
    
    def getage(self):
        return '{0} is {1} years old. '.format(self.name, self.age)	
            
    def sing(self):
        return '{0} is now singing'.format(self.name)

		
