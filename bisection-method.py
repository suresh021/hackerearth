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

error=0.0000000000001

a=100
b=-100
mid= (a+b)/2.0
itr=1


result=bisect(func,a,b,error)
print("Root:"+str(result))
