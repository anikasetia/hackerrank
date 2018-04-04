s = list(input())
i = 0
while(i < len(s) - 1):
	if(s[i] == s[i+1]):
		s.pop(i)
		s.pop(i)
		i = 0
	else:
		i += 1

newString = (''.join(s))

if(newString == ''):
	print("Empty String")
else:
	print(newString)
