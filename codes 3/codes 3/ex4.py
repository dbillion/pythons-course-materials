# sum function that takes variable number of arguments
def summ(v1, *rest):
    print(type(v1)) 
    print(type(rest))
    return (v1 + sum(rest))


#print("summation", summ(1, 2, 3, 4))







	
	
