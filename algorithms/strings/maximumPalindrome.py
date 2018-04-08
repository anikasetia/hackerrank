def fact(n):
	ans = 1
	for i in range(1,n+1):
		ans *= i
	return ans

def pallindromes(string):
	charMap = {}
	for i in range(len(string)):
		if(string[i] in charMap):
			charMap[string[i]] += 1
		else:
			charMap[string[i]] = 1
	singles = 0
	freq = 0
	den = 1
	num = 0
	for each in charMap:
		if(charMap[each] %2 != 0):
			singles += 1
		freq = charMap[each] // 2
		num += freq
		den = den * fact(freq)

	if(num != 0):
		num = fact(num)
	
	ans = num//den

	if(singles!=0):
		ans = ans*singles
	
	return (ans%1000000007)
		
			 



s = input()
q = int(input())
lr = []

for i in range(q):
	item = input().strip().split(' ')
	item = [int(item[0]), int(item[1])]
	lr.append(item)

for each in lr:
	string = s[each[0]-1:each[1]]
	print(pallindromes(string))
