# function definition
#########################

def calcTemp(F):
    frht = float(F)
    cel = (frht - 32.0) * (5.0/9.0)
    return cel


def safeDivision(value1, value2):
	try:
		value1 = float(value1)
		value2 = float(value2)
		return value1/value2
	except ZeroDivisionError:
		return 1.0E100

		
		