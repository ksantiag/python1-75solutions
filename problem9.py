#problem9

a = [6,103,77,49,0,83,77,77,444,444]
b = 77

def removeB(a, b):
   count = 0
   j = 0
   for i in range(0,len(a)):
      if a[i] == b:
         count = count + 1
   
   newArr = [0]*(len(a) - count)
   
   for i in range(0, len(a)):
      if a[i] != b:
         newArr[j] = a[i]
         j = j+1
         
   return newArr;     
   
newArr = removeB(a,b)

print newArr   
   

          