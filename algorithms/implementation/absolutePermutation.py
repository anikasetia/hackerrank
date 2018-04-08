def getPermutations(n, k):
	perm = []
	perm1 = []
	perm2 = []

	for i in range(1, n+1):
		val1 = k + i
		val2 = -k + i
		
		if(0 < val1 and val1 < n+1):
			perm.append(str(val1))
		elif(0 < val2 and val2 < n+1):
			perm.append(str(val2))
	if(len(perm) == n):
		print(" ".join(perm))
	else:
		print("-1")
T = int(input())
for i in range(T):
	n, k = input().strip().split(' ')
	n, k = [int(n), int(k)]

	getPermutations(n,k)
