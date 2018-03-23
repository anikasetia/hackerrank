def getX(x,p):
	for i in range(0,len(p)):
		if(x == p[i]):
			return i + 1

n = int(input())
p = input().split(" ")

for i in range(0,n):
	p[i] = int(p[i])

for i in range(0, n):
	print(getX(getX(i+1, p),p))
