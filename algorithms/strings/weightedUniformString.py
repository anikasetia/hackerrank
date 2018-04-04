def stringWeight(string):
	weight = 0
	for i in range(len(string)):
		weight += ord(string[i]) - ord('a') + 1
	return weight

string = input()
n = int(input())

weights = []

for i in range(0, n):
	weights.append(int(input()))

weightMap = {}
i = 0
while(i < len(string)):
	start = string[i]
	if(not(start in weightMap)):
		weightMap[start] = stringWeight(start)
	i += 1
	while((i < len(string)) and (start[len(start) - 1] == string[i])):
		start += string[i]
		if(not(start in weightMap)):
			weightMap[start] = stringWeight(start)
		i += 1

for weight in weights:
	found = False
	for item in weightMap:
		if(weightMap[item] == weight):
			found = True
			print("Yes")
			break
	if(not found):
		print("No")
