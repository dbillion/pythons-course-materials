####parent class
class Bird:
    def __init__(self):
        print('Bird is hatched')

    def whois(self):
        print('Bird')

    def fly(self):
        print('flying high')


class Parrot(Bird):
    def fly(self):
        print('parrot can fly')

    def swim(self):
        print('parrot cant swim')


class Penguin(Bird):
    def fly(self):
        print('penguins cant fly')

    def swim(self):
        print('penguins can swim')

######class definitions ends

# common interface
def flying_test(bird):
    print(type(bird))
    bird.fly()
	
#####instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)

# print(isinstance(blu, Parrot))
# print(issubclass(Parrot, Bird))
