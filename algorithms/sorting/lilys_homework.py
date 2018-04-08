n = int(input())
l = list(map(int, input().strip().split(' ')))

unsorted = []

for each in l:
	unsorted.append([each, 0])

l.sort()

swaps = 0
for i in range(n):
	nodes = 0
	if(unsorted[i][1] == 0):
		unsorted[i][1] = 1
		pos = l.index(unsorted[i][0])
		if(pos != i):
			nodes += 1
			while(unsorted[pos][1] != 1):
				nodes += 1
				unsorted[pos][1] = 1
				pos = l.index(unsorted[pos][0])

		if(nodes > 0):
			swaps = swaps + (nodes - 1)
print(swaps)
