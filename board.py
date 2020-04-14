
game = [
[0,0,0],
[0,0,0],
[0,0,0]
]

moves = {
	(0,0): [(1,0),(1,1),(0,1)],
	(1,0): [(0,0),(1,1),(2,0)],
	(2,0): [(1,0),(1,1),(2,1)],
	(0,1): [(0,0),(1,1),(2,0)],
	(1,1): [(0,0),(1,0),(2,0),(0,1),(2,1),(0,2),(1,2),(2,2)],
	(2,1): [(2,0),(1,1),(2,2)],
	(0,2): [(0,1),(1,1),(1,2)],
	(1,2): [(0,2),(1,1),(2,2)],
	(2,2): [(1,2),(1,1),(2,1)]
}

gaps = {
	(0,0): [(2,0),(2,2),(0,2)],
	(1,0): [(1,2)],
	(2,0): [(0,0),(0,2),(2,2)],
	(0,1): [(2,1)],
	(1,1): [],
	(2,1): [(0,1)],
	(0,2): [(0,0),(2,0),(2,2)],
	(1,2): [(1,0)],
	(2,2): [(0,0),(0,2),(2,0)]
}

def printBoard():
	for i in range(0,3):
		print(game[i][0],"|",game[i][1],"|",game[i][2])
		#print("_   _   _")

def move(coords,value):
	x = coords[0]
	y = coords[1]
	if (((0 <= x < 3) and (0 <= y < 3))) and (game[y][x] == 0):
		game[y][x] = value
		checkIfWin()
		return True
	else:
		print("Not a valid move")
		return False

def isValidMove(coords):
	x = coords[0]
	y = coords[1]
	return game[y][x] == 0

def checkIfWin():
	#todo check for win condition
	pass

def isEmpty():
	empty = True
	for i in game:
		for j in i:
			empty = empty and j == 0
	return empty

def isFull():
	full = True
	for i in game:
		for j in i:
			full = full and j != 0
	return full

def getPerimiter(coords):
	return moves[coords]

def getGaps(coords):
	return gaps[coords]

def getOpenSpaces():
	availble = []
	for y in game:
		for x in y:
			if x == 0:
				availble.append((x,y))
	return availble

def isOpen(coords):
	return game[coords[1]][coords[0]] == 0

def getValue(coords):
	return game[coords[1]][coords[0]]