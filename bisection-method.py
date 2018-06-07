# Bisection Method to find root of polynomial



def bisect(func,a,b,error):
	iteration=1
	if((func(a)*func(b))<0):
		print("These initial values do not bracket the result.")
	else:
		while (abs(b-a)>error):
			mid=(a+b)/2.0
			print("Iteration:"+str(iteration))
			iteration+=1
			if((func(a)*func(mid))>0):
				a=mid
			else:
				b=mid
		return mid
		
def func(x):
	return (x**4-6) # function


error=0.0000000000001 #max error
a=100 # first guess
b=-100 # second guess
mid= (a+b)/2.0 # mid value

result=bisect(func,a,b,error)
print("Root:"+str(result))
