class Generic(object):
    '''test class'''
    
    def __init__(self,number):
        self.number = number
        
    def factorial(self):
        fact = 1
        while(self.number!=1):
            fact = fact * self.number
            self.number -=1
        return fact
    

word = input()
number = int(word) # cast the input string to integer type 
newObj = Generic(number)
print (newObj.factorial())
