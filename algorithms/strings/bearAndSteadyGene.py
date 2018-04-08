def validate(geneMap):
	valid = True

	for key in geneMap:
		if(geneMap[key] <= n//4):
			valid = False
			break
	return valid



n = int(input())
s = input()

geneMap = {'A':0, 'C':0, 'T':0, 'G':0}

for i in range(n):
	if(s[i] in geneMap):
		geneMap[s[i]] += 1
print(geneMap)
valid = validate(geneMap)
if(valid):
	print(0)
else:
	i = 0
	ans = 999999999999999999
	for j in range(0,n):
		geneMap[s[j]] -= 1
		while((not validate(geneMap)) and i <= j):
			ans = min(ans, j-i+1);
			geneMap[s[i]] += 1
			i += 1
	
	print(ans)
