a=256
def maximum(b,n):
  count=[0]*a
  for i in range(n): 
      count[ord(str[i])]+=1
   x=0
   for i in range(a): 
      if (count[i]!=0): 
          x+=1    
   return x 
def smallsubstring(b): 
    n=len(b)    
    x=maximum(b, n) 
    y=n
    for i in range(n): 
        for j in range(n): 
            s=str[i:j] 
            s1=len(subs) 
            s2=maximum(s,s1)  
            if (s1<y and x==s2): 
                y=s1 
    return y 
l=smallsubstring(b)
b=str(input())
print(l)
