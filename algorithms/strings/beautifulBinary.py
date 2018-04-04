n = int(input())
s = input()
print((n - len(s.replace("010", "")))//3)
