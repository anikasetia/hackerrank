n = int(input())
c = list(map(int, input().strip().split(' ')))

c.sort()

miles = 0
j=0
for i in range(len(c)-1, -1, -1):
	miles += pow(2,j) * c[i]
	j += 1

print(miles)
