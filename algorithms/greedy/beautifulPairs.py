n = int(input())
A = list(map(int, input().strip().split(' ')))
B = list(map(int, input().strip().split(' ')))

disjointSets = []

i = 0
j = 0

toSkipJ = []
while(i<len(A)):
	j = 0
	while(j<len(B)):
		if(A[i] == B[j] and (not(j in toSkipJ))):
			disjointSets.append([i,j])
			toSkipJ.append(j)
			i += 1
			j += 1
		else:
			j += 1
	i += 1
print(len(disjointSets) + 1)

