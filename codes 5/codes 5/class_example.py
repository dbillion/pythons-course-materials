class Student:
    ''' a sample class '''
    sp = 'SE'                       # Class Variable (static variables) 
    gp = []                         # shared by all objects of same class

    def __init__(self, n): 
        self.name = n               # Instance Variable (attributes)

    def get(self):
        return self.name

##end of class

s1 = Student('Ken')
s2 = Student('Li')

##print(s1.get())
##print(s2.get())
##
##print(s1.sp)
