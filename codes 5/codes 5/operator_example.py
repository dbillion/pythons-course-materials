class Point:
	'''A class to describe the x,y coordinates (cartesian) in 2D plane'''
	
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
		print('default constructor is called')
	
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Point(x, y)
		
	def __str__(self):
		return '({0},{1})'.format(self.x, self.y)
		
## end of class

p1 = Point(2,3)
p2 = Point(-1, 4)
p3 = p1 + p2 
print( p3 )
print(type(p3))
print(type(str(p3)))
# '{} point is used'.format(p2)













	
	


# print(str(p1))
