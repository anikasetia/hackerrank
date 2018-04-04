n = int(input())
strings = []

for i in range(n):
	strings.append(list(input()))

for each in strings:
	print(len(set(each)))
