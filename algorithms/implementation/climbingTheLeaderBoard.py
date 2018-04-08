def getRanks(board_scores, rank):

	for i in range(1, len(board_scores)):
		if(board_scores[i-1] > board_scores[i]):
			rank.append(rank[i-1] + 1)
		else:
			rank.append(rank[i-1])

n  = int(input())
board_scores = list(map(int, input().strip().split(' ')))
alice_count = int(input())
alice = list(map(int, input().strip().split(' ')))

rank = [1]
getRanks(board_scores, rank)

j = len(board_scores) - 1
i = 0
while(i<len(alice)):
	while(j >=0 ):
		if(alice[i] < board_scores[j]):
			print(rank[j] + 1)
			i += 1
			j -= 1
		elif(alice[i] == board_scores[j]):
			print(rank[j])
			i += 1
			j -= 1
		else:
			j -= 1
	if(alice[i] > board_scores[0]):
		print(1)
		i += 1

#rank.sort(reverse = True)
#print(rank)
