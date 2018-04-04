def checkValid(s1, s2, s3):
	if(((s1 + s2) > s3) and ((s2 + s3) > s1) and ((s1 + s3) > s2)):
		return True
	else:
		return False

n = int(input())
sticks = list(map(int, input().strip().split(' ')))
sticks.sort()

valid = False
for i in range(len(sticks) - 1,-1,-1):
	valid = checkValid(sticks[i], sticks[i-1], sticks[i-2])
	if(valid):
		print(str(sticks[i-2]) + " " + str(sticks[i-1]) +" "+ str(sticks[i]))
		break

if(not valid):
	print("-1")
