
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

corners = {
	(0,0): True,
	(1,0): False,
	(2,0): True,
	(0,1): False,
	(1,1): False,
	(2,1): False,
	(0,2): True,
	(1,2): False,
	(2,2): True
}

def printBoard():
	for i in range(0,3):
		print(game[i][0],"|",game[i][1],"|",game[i][2])
		#print("_   _   _")
	print()

def move(coords,value):
	if isFull():
		print("cant move")
	x = coords[0]
	y = coords[1]
	if (((0 <= x < 3) and (0 <= y < 3))) and (game[y][x] == 0):
		game[y][x] = value
		if checkIfWin(value):
			print(value, "wins!")
			printBoard()
			exit(0)
		return True
	else:
		print("Not a valid move")
		return False

def isValidMove(coords):
	x = coords[0]
	y = coords[1]
	return game[y][x] == 0

def checkIfWin(value):
	top = (getValue((0,0)) == getValue((1,0)) == getValue((2,0)) == value)
	middle = (getValue((0,1)) == getValue((1,1)) == getValue((2,1)) == value)
	bottom = (getValue((0,2)) == getValue((1,2)) == getValue((2,2)) == value)
	left = (getValue((0,0)) == getValue((0,1)) == getValue((0,2)) == value)
	center = (getValue((1,0)) == getValue((1,1)) == getValue((1,2)) == value)
	right = (getValue((2,0)) == getValue((2,1)) == getValue((2,2)) == value)
	diag1 = (getValue((0,0)) == getValue((1,1)) == getValue((2,2)) == value)
	diag2 = (getValue((2,0)) == getValue((1,1)) == getValue((0,2)) == value)
	rows = [top, middle, bottom, left, center, right, diag1, diag2]
	if top or middle or bottom or left or center or right or diag1 or diag2:
		for i in rows:
			print(i)
	return top or middle or bottom or left or center or right or diag1 or diag2


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

def isCorner(coords):
	return corners[coords]

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

def clear():
	global game
	game = [
	[0,0,0],
	[0,0,0],
	[0,0,0]
	]
