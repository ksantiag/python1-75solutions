#Problem7

a = input("Enter a: ")
type(a)

b = input("Enter b: ")
type(b)

result = a
#for loop
for i in range(0,4):
   result *= a   
   
#Math.pow is just pow(a,b) in python
#result = pow(a, b)



print "The grand total is "+str(result)
