class Sample:
    
    def __init__(self):
        print('constructor called automatically when object created')
    
    def __del__(self):
        print('destructor called automatically.. object destroyed')
        
#end of class
s = Sample()
del s
