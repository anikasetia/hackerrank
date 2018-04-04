n, k = input().strip().split(' ')
n, k = [int(n), int(k)]

contests = []
balance = 0
for i in range(n):
	luck, importance = input().strip().split(' ')
	luck, importance = [int(luck), int(importance)]
	if(importance == 0):
		balance += luck
	else:
		contest = [luck, importance]
		contests.append(contest)
contests.sort()
last = len(contests)

if(k < len(contests)):
	for i in range(len(contests) - 1, len(contests) - k -1, -1):
		balance += contests[i][0]
		last -= 1

	for i in range(0,last):
		balance -= contests[i][0]

else:
	for i in range(len(contests)):
		balance += contests[i][0]	
print(balance)


