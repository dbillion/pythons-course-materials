class Car:
    ''' modeling of cars'''
    #rims = [] # class instance
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0
        self.rims = []
    
    def update_odometer(self, km):
        if km >= self.odometer:
            self.odometer = km
        else:
            print('it is illegal to reverse the meter')
    
    def increment_odometer(self, increment = 100):
        self.odometer += increment
    
    def add_rims(self, r):
        self.rims.append(r)
    
    def get_info(self):
        print( '''
                Car Manufacturer: {}
                Car Model: {}
                Car Year: {}
                Car Milage: {}
                '''.format(self.brand,
                           self.model,
                           self.year,
                           self.odometer))
        if len(self.rims):
            print('''
                Car Rim: {}
                '''.format(self.rims))
# end of class
c1 = Car('toyota', 'prius', 2010)
c2 = Car('BMW', '320', 2016)
c1.get_info()

