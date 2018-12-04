#problem13

store = [0] * 10000

i = 0
count = 0

while store[i] < 2:
   i = input("Enter an int: ")
   type(i)
   
   store[i] += 1
   count += 1

print "You entered "+str(count)+" value."   
