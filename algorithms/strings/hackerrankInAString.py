n = int(input())
strings = []
checker = "hackerrank"
for i in range(n):
	strings.append(input())
for each in strings:
	j = 0
	for i in range(len(each)):
		if(each[i] == checker[j]):
			j += 1
		if(j == len(checker)):
			print("YES")
			break
	if(j < len(checker)):
		print("NO")
