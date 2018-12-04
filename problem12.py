#problem12

a = input("Enter a: ")
type(a)

b = input("Enter b: ")
type(b)

c = input("Enter c: ")
type(c)

#big = max(a, b, c)

if (a > b) & (a > c):
   big = a
elif (b > a) & (b > c):
   big = b
else:
   big = c      

count = 0

if a == big:
   count += 1
if b == big:
   count += 1
if c == big:
   count += 1   
      
   
print "The largest integer "+str(big)

if count == 1:
   print "was entered once."
elif count == 2:
   print "was entered twice."
else:
   print "was entered three times."              
      