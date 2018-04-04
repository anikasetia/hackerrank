numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
length = int(input())
s = input()
longEnough = False
numberPresent = False
lowercasePresent = False
uppercasePresent = False
specialCharacterPresent = False

needed = 0

if(len(s) >= 6):
	longEnough = True
for i in range(0,len(s)):
	if(s[i] in numbers):
		numberPresent = True
	elif(s[i] in lower_case):
		lowercasePresent = True
	elif(s[i] in upper_case):
		uppercasePresent = True
	elif(s[i] in special_characters):
		specialCharacterPresent = True

if(not specialCharacterPresent):
	needed += 1
if(not uppercasePresent):
	needed += 1
if(not lowercasePresent):
	needed += 1
if(not numberPresent):
	needed += 1

if((len(s) + needed) < 6):
	needed += (6 - (len(s) + needed))

print(needed)
