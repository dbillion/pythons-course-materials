##mytuple = ('helo')
##print(type(mytuple))

### need a comma at the end
##mytuple = ('hello',)  
##print(type(mytuple))

### parentheses is optional
##mytuple = 'hello',
##print(type(mytuple))
##
##mytuple = 1,
##print(type(mytuple))
##
##mytuple = ('p','e','r','m','i','t')
##print(mytuple[0])
##print(mytuple[-1])
##print('a' in mytuple)
##print('s' not in mytuple)

##nested tuple
##item of mutable element can be changed
t = ('University', [8, 4, 6], (1, 2, 3))
print(t[0][3])
print(t[1][1])

t[1][1] = 9
print(t[1])
##
####t[1] = 6, 7, 8,
####print(t)
####TypeError: 'tuple' object does not support item assignment
####however complete new assignment is never forbidden in python
##t = ('new university', (2, 3, 1), [8, 4, 6])
##print(t)
##
##del mytuple
##print(mytuple)
