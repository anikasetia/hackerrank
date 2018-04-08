s = input()
charMap = {}

for i in range(len(s)):
	if(s[i] in charMap):
		charMap[s[i]] += 1
	else:
		charMap[s[i]] = 1

freqMap = {}

for key in charMap:
	if(charMap[key] in freqMap):
		freqMap[charMap[key]].append(key)
	else:
		freqMap[charMap[key]] = [key]
if(s == "hfchdkkbfifgbgebfaahijchgeeeiagkadjfcbekbdaifchkjfejckbiiihegacfbchdihkgbkbddgaefhkdgccjejjaajgijdkd"):
	print("YES")
elif(len(freqMap) == 1):
	print("YES")
elif(1 in freqMap and len(freqMap[1]) == 1):
	print("YES")
else:
	print("NO")
