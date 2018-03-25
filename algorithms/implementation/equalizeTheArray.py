n = int(input())
a = input().split()
counts = {}
maxim = 0
'''for each in a:
	if(each in counts):
		counts[each] = counts[each] + 1
	else:
		counts[each] = 1
'''

while(len(a) > 0):
	valToRem = a[0]
	elementCount = a.count(valToRem)
	if(maxim < elementCount):
		maxim = elementCount
	#print(elementCount)
	a = list(filter(lambda x:x!=valToRem, a))
	#print(a)

print(n-maxim)
#print(a)
#maxkey = (max(counts))
#print(n - counts[maxkey])	
