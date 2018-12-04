#problem11

a = 3
b = 6

def rangeProduct(a,b):
   product = 1
   # the +1 is going to the same as <=
   for i in range(a, b+1):
      product *= i
      
   return product
   
result = rangeProduct(a,b)
print result     
      