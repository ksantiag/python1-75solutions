#problem14

A = [3,8,5,2,7,9]
B = [5,1,22,7,9,15,3]

def largestInCommon(A,B):
   max = A[0]
   match = A[0]
   
   for i in range(len(A)):
      for j in range(len(B)):
         if B[j] == A[i]:
            match = A[i]
            if match > max:
               max = match
   return max;

result = largestInCommon(A,B)

print result                    
            