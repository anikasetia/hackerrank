n = int(input())

strings = []

for i in range(n):
	strings.append(input())

for each in strings:
	if(each[0] == '0'):
		print("NO")
	else:
		found = False
		for i in range(1, len(each)):
			initialStart = each[0:i]
			start = each[0:i]
			startInt = int(each[0:i])
			while(len(start) < len(each)):
				if(start == each[0:len(start)]):
					start += str((startInt) + 1)
					startInt += 1
				else:
					break
			if(start == each):
				print("YES " + initialStart)
				found = True
				break
		if(not found):
			print("NO")
