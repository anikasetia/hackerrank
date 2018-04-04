def surfaceArea(A):
	a = [[0] * (len(A[0]) + 2)]
	for row in A:
		a.append([0] + row + [0])
	a.append([0] * (len(A[0]) + 2))

	ans = len(A) * len(A[0]) * 2

	for i in range(1,len(a)):
		for j in range(1,len(a[i])):
			ans += abs(a[i][j] - a[i-1][j])
			ans += abs(a[i][j] - a[i][j-1])
	return ans

if __name__ == "__main__":
	H, W = input().strip().split(' ')
	H, W = [int(H), int(W)]

	A = []
	for A_i in range(H):
		A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
	result = surfaceArea(A)
	print(result)
