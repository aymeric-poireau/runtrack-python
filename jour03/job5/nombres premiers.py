
min = int(2)
max = int(1000)
for n in range(min,max + 1):
   if n < 1001:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)