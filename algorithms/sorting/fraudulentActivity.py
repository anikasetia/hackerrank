import bisect

def countSort(arr):
	expTrack = [0 for i in range(0,201)]
	for each in arr:
		expTrack[each] += 1
	res = []
	for i in range(201):
		if(expTrack[i] != 0):
			for j in range(expTrack[i]):
				res.append(i)
	return res


n, d = input().strip().split(' ')
n, d = [int(n), int(d)]

exp = list(map(int, input().strip().split(' ')))

notifs = 0
window = countSort(exp[0:d])

for i in range(n-d-1):
	if(d%2 == 0):
		if(exp[i+d] >= 2*(window[d//2])):
			notifs += 1
	else:
		if(exp[i+d] >= (window[d//2] + window[(d-1)//2] )):
			notifs += 1
	window.remove(exp[i])
	bisect.insort(window, exp[i+d])
'''for i in range(n-d-1):
	x = countSort(exp[i:i+d])
	if(d%2 == 0):
		if(exp[i+d] >= 2*(x[d//2])):
			notifs += 1
	else:
		if(exp[i+d] >=  (x[d//2] + x[(d-1)//2] )):
			notifs += 1
'''
print(notifs)
