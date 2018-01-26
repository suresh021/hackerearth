# Problem
# You have been given a positive integer N. You need to find and print the Factorial of this number.

word = input()
number = int(word) # cast the input string to integer type 
result = 1
while(number!=1):
    result = result * number
    number -=1
    
print (result)
