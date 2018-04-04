n = int(input())
arr = list(map(int, input().strip().split(' ')))
arr.sort()
minDiff = max(arr)
for i in range(0,len(arr)-1):
	minDiff = min(minDiff, abs(arr[i] - arr[i+1]))
print(minDiff)
