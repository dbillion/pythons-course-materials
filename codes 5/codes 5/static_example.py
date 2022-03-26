class ClassName:
    def member_method(self):
        print('hello')
            
    @staticmethod
    def add(x,y):
        return x + y


## end of class

s = ClassName.add(3,4)
# x = ClassName()
# x.member_method()
# x.add(3,4)

print('result is ', s)
print(type(s))
