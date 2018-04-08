def getArea(n):
	return (2*n - 1)

def getPluses(grid, i, j):
	cellCoords = [(i,j)]
	size = 1
	for n in range(1,15):
		if(grid[i-n][j] == "G" and grid[i+n][j] == "G" and grid[i][j-n] == "G"  and grid[i][j+n] == "G"):
			size += 2
			cellCoords.append((i-n, j))
			cellCoords.append((i+n, j))
			cellCoords.append((i, j-n))
			cellCoords.append((i, j+n))
		else:
			break
	return [size, cellCoords]


def getPluses2(grid, i, j, cellCoords):
	size = 1
	for n in range(1,15):
		if(grid[i-n][j] == "G" and grid[i+n][j] == "G" and grid[i][j-n] == "G"  and grid[i][j+n] == "G"):
			
			if(not(((i-n, j) in cellCoords) or ((i+n, j) in cellCoords) or ((i, j-n) in cellCoords) or ((i, j+n) in cellCoords))):
				size += 2
			else:
				break
		
		else:
			break
	return size

	

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
grid = []
topString = "".join(['B' for x in range(n+3)])
grid.append(topString)
for i in range(n):
	grid.append("B" + input() + "B")
	
grid.append(topString)
maxSize = 0
maxCellCoords = []
for i in range(1,n+1):
	for j in range(1,m+1):
		if(grid[i][j] == "G"):
			currSizeValues = (getPluses(grid, i, j))
			currSize = currSizeValues[0]
			if(currSize > maxSize):
				maxSize = currSize
				maxCellCoords = currSizeValues[1]

secondMaxSize = 0
for i in range(1,n+1):
	for j in range(1,m+1):
		if(grid[i][j] == "G"):
			currSize = getPluses2(grid, i, j, maxCellCoords)
			if(secondMaxSize < currSize):
				secondMaxSize = currSize


print(getArea(maxSize) * getArea(secondMaxSize))
