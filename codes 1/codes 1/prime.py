#function to check if the number is prime. 

def is_prime(number):
	if number <= 1:
		return False
	for n in range(2, number):
		if number % n == 0:
			return False
	else:
		return True
# end of function
