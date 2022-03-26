class ComplexNumber:
    ''' a sample class '''
    
    def __init__(self, r, im):
        self.real = r
        self.imag = im
        
    def disp(self):
        print('{} + {}j'.format(self.real, self.imag))
        
# end of class definition
