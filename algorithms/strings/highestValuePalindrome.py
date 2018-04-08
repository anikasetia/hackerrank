n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
s = input()

changePoints = 0
changePointsCollection = []
for i in range(n//2 -1, -1, -1):
	print(i, n-i-1)
	if(s[i] != s[n-i-1]):
		changePointsCollection.append((i,n-i-1))
		changePoints += 1

print(changePoints)
print(changePointsCollection)

if(changePoints >  k):
	print(-1)
else:
	listMap = list(s)
	for each in changePointsCollection:
		val = max(int(listMap[each[0]]), int(listMap[each[1]]))
		listMap[each[0]] = str(val)
		listMap[each[1]] = str(val)
		k -= 1
	i = 0
	while(k > 0):
		if((i,n-1-i) in changePointsCollection):
			listMap[i] = "9"
			listMap[n-1-i] = "9"
			k-=1
		i += 1
	print("".join(listMap))
