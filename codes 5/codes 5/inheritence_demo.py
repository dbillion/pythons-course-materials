class A:
    ''' sample A '''
    
    def __init__(self):
        self.name = 'A'
    
    def info(self):
        print(self.name)


class B(A):
    
    def __init__(self):
        super().__init__()
        self.other_name = 'B'
    
    def info(self):
        print(self.name)
        print(self.other_name)
