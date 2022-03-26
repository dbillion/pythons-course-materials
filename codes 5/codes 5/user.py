##Make a class called User Create two attributes called first_name
##and last_name, and then create several other attributes that are typically stored
##in a user profile Make a method called display_user() that prints a summary
##of the user’s information. Make another method called greet_user() that prints
##a personalized greeting to the user
##    - Create several instances representing different users, and
## call both methods for each user
##
##
##
##Write a method called increment_login_attempts() that increments the value of login_attempts by 1
##everytime login() method is called for the user. Write
##another method called reset_login_attempts() that resets the value of login_attempts to 0
##Make an instance of the User class and call login() severl time to increment the counter using
##increment_login_attempts().. Print the value of login_attempts to make sure it was incremented
##properly, and then call reset_login_attempts(). Print login_attempts again to mke sure it was reset to 0
##
##Create few users and list them in the order based on the first_name,
##second_name or age. 

class User:
    ''' User class to record information of users login logout'''
    total_user = [0] # class instance keeping tabs on how many registered users
    
    def __init__(self, fn, sn, ag, gen):
        self.fname = fn
        self.sname = sn
        self.age = ag
        self.gender = gen
        self.login_attempts = 0
        self.total_user[0]  += 1 
    
    #user login func 
    def login(self):
        print(self.fname.capitalize() + ' has logged in.')
        self.increment_login_attempts()
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
    # display user info
    def display_user(self):
        print('User Information:')
        print(' - First Name: {}'.format(self.fname))
        print(' - Second Name: {}'.format(self.sname))
        print(' - Age: {}'.format(self.age))
        print(' - Gender: {}'.format(self.gender))
        print(' - Login Attempts: {}'.format(self.login_attempts))

    
#     @staticmethod
#     def all_users():
#         print('Total Users in the system: {}'.format(.total_user[0]))



##end of class

u1 = User('tom', 'Verceti', 19, 'male')

