s = input()
count = 0
for i in range(0, len(s)):
	if(ord('A') <= ord(s[i]) <= ord('Z')):
		count +=1

count += 1

print(count)
