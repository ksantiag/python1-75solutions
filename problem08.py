#problem8

A = [6,8,15,22,77,93,98]

B = [5,15,22,44,93]


def howManyInCommon(A, B):

   count = 0
   #A.length looks like in python len(A)
   for i in range(len(A)):
      for j in range(0,len(B)):
         if B[j] == A[i]:
            count = count + 1
         
   return count
   
#has to be called after method/function is already coded   
count = howManyInCommon(A, B) 

print count    
