# Bisection Method to find root of polynomial

coeff_0=7
coeff_1=-5
coeff_2=1
error=0.001

a=7
b=4
mid= (a+b)/2
itr=1

def func(val):
	return (val*val-5*val+6) # function is x^2-sx+6

if((func(a)*func(b))<0):
	print("These initial values do not bracket the result.")
else:
	while ((mid-a)>error):
		print("Iteration:"+str(itr))
		itr+=1
		if((func(a)*func(mid))>0):
			a=mid
		else:
			b=mid

		mid=(a+b)/2



print("Root:"+str(mid))
