class Computer:
    ''' an example class to sell computer '''
    
    def __init__(self):
            self.__maxprice = 900
            self._originalprice = 1500

    def sell(self):
            print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
            self.__maxprice = price
    
    def _showmaxprice(self):
            print(self.__maxprice)

## end of class

c = Computer()
# c.sell()
# print(c._originalprice)
#print(c.__maxprice)
##print('accsing private data:' c._Computer__maxprice)
# c.sell()

# # change the price
##print('trying to change the private data outside the class')
##c.__maxprice = 1000
##c.sell()

# print('price can sell be set by calling appropriate function')
# # using setter function
# c.setMaxPrice(1000)
# c.sell()

# c._showmaxprice()
