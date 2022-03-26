class Dog():
    '''A simple class to model a dog.'''
    
    family = 'canine'               # Class Variable (static variables) 
    #gp = []                        # shared by all objects of same class
    #tricks = []
    
    def __init__(self, name, age):
        '''Initialize name and age attributes.'''
        self.name = name
        self.age = age
        self.tricks = []
    
    def add_trick(self, trick):
        '''Dog is learning a new trick. '''
        self.tricks.append(trick)
    
    def sit(self):  
        '''Simulate a dog sitting in response to a command.'''
        print(self.name.title() + ' is now sitting.')
    
    def roll_over(self):
        '''Simulate rolling over in response to a command.'''
        print(self.name.title() + ' rolled over!')
        
    def description(self):
        print("My dog's name is " + self.name.title() + '.')
        print('My dog is ' + str(self.age) + ' years old.')
        
        
