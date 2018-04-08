s1 = input()
s2 = input()

Board = []

for i in range(len(s2) + 1):
	Board.append([0 for i in range(len(s1) + 1)])

for i in range(len(s1)):
	for j in range(len(s2)):
		if(s1[i] == s2[j]):
			Board[j+1][i+1] = Board[j][i] + 1
		else:
			Board[j+1][i+1] = max(Board[j][i+1], Board[j+1][i])

print(Board[len(s2)][len(s1)])
