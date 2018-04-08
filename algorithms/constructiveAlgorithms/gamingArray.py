g = int(input())

for game in range(g):
	n = int(input())
	A = list(map(int, input().strip().split(' ')))
	
	count = 0
	maxim = 0

	for i in range(n):
		if(maxim < A[i]):
			maxim = A[i]
			count += 1
	if(count % 2 ==0):
		print("ANDY")
	else:
		print("BOB")
