n = int(input())
c = input().split()

i = 0
jumps = 0
while(i < n-1):
	if(c[i+2] == "1"):
		i = i + 1
	else:
		i = i + 2

	jumps = jumps + 1

print(jumps)
