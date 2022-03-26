### dictionary with integer keys
##mydict1 = {1: 'apple', 2: 'ball'}
##
### dictionary with mixed keys
##mydict2 = {'name': 'John', 'age': 33}
##
### using dict()
##mydict3 = dict({1:'apple', 2:'ball'})
##
### from sequence having each item as a pair
##mydict4 = dict([(1,'apple'), (2,'ball')])
##
### Output:
##print(mydict2['name'])
##
###Output: error when called with []
##print(mydict2['age'])
##
##print(mydict2['age'])
##print(mydict2.get('age'))
##
### update value
##mydict2['age'] = 27
##
###update with method
##mydict2.setdefault('address', 'city center')

###How the dictionary looks like. 
##print(mydict2)

# create a dictionary
# Dictionary comprehension. 
squares = {n : n ** 2 for n in range (1, 6)}
squares2 = {1:1, 2:4, 3:9, 4:16, 5:25}  
##
### remove a particular item
### Output: 16
##print(squares.pop(4))  
##
### Output: {1: 1, 2: 4, 3: 9, 5: 25}
##print(squares)
##
### remove an arbitrary item
### Output: (1, 1)
##print(squares.popitem())
##
### Output: {2: 4, 3: 9, 5: 25}
##print(squares)
##
### delete a particular item
##del squares[1]  
##
### Output: {2: 4, 3: 9}
##print(squares)
##
### remove all items
##squares.clear()
##
### Output: {}
##print(squares)
##
### delete the dictionary itself
##del squares
##
### Throws Error
##print(squares)
##
##print(1 in squares)
##
##print(2 not in squares)
##
##print(49 in squares)
##
##squares = {x: x*x for x in range(11) if x%2 != 0}
##for i in squares:
##    print(squares[i])
##
##print(len(squares))
##
##print(sorted(squares))
