def totNum(x, n, num):
	if(pow(num,n) < x):
		return totNum(x,n,num+1) + totNum(x - pow(num,n), n, num + 1)
	elif(pow(num, n) == x):
		return 1
	else:
		return 0;


x = int(input())
n = int(input())
count = 0

print(totNum(x,n,1))
