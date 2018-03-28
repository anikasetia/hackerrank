T = int(input())
lengths = []
strings = []
charCounts = {'_':0}

for i in range(65,91):
	#print(chr(i))
	charCounts[str(chr(i))] = 0

for i in range(T):
	lengths.append(int(input()))
	strings.append(input())

for each in strings:
	unhappy = False
	if('_' in each):
		for i in range(len(each)):
			charCounts[each[i]] += 1
		for key in charCounts:
			if key != '_':
				if(charCounts[key] == 1):
					print("NO")
					unhappy = True
					break
		if(not unhappy):
			print("YES")
		for key in charCounts:
			charCounts[key] = 0
	else:
		for i in range(len(each)):
			if(len(each) == 1):
				unhappy = True
				print("NO")
				break
			elif(i==0):
				if(each[i] != each[i+1]):
					unhappy = True
					print("NO")
					break
			elif(i==len(each)-1):
				if(each[i] != each[i-1]):
					unhappy = True
					print("NO")
					break
			if(not ((each[i-1] == each[i]) or (each[i] == each[i+1]))):
				unhappy = True
				print("NO")
				break
		if(not unhappy):
			print("YES")
			
#print(charCounts)
#print(lengths)
#print(strings)
		
