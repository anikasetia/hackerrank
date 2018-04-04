n = int(input())

i = 0
count = 0
while(i<n):
	if((n + i) == (n ^ i)):
		count += 1
	i += 1
print(count)
