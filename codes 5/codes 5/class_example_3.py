class Seed:
    ''' from the creation to destruction '''
    
    def __init__(self, name):
        self.x = 0
        self.name = name
        print('{} is alive.'.format(self.name))
        
    def growing(self):
        self.x = self.x + 1
        
    def __del__(self):
        print('{} is destroyed.'.format(self.name))

# end of class

z = Seed('z')
z.growing()
print(type(z))
z = 'another variable assignment'
print(z)
print(type(z))
 
s = Seed('s')
s = 123 