import math
import sys

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

c.sort()

a=0

i=0

while(i<len(c)-1):
    max_l=(c[i+1]-math.ceil((c[i]+c[i+1])/2))
    a=max_l if (a<max_l) else a
    i+=1


max_2=c[0]
max_3=n-1-c[len(c)-1]

print(max(a,max_2,max_3))
