#problem10
`
a = [88,88,88,63,29,77,77,77,77,50,44,44,8,0,99,99]

def indexOfFirstPair(a):
   index = -1
   
   for i in range(1, (len(a)-2)):
      if (a[i-1] != a[i]) & (a[i] == a[i+1]) & (a[i+1] != a[i+2]):
         index = i
         return index;

result = indexOfFirstPair(a)   
   
print result      
      
   