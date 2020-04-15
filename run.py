import board
from Allan import Allan

myValue = 2
allan = Allan(1)
board.printBoard()
while board.checkIfWin != True:
	x = int(input("x: "))
	y = int(input("y: "))
	print()
	board.move((x,y), myValue)
	board.printBoard()
	allan.makeMove()
	board.printBoard()
	if board.isFull():
		board.clear()
		board.printBoard()


board.printBoard()
print("Game Over")
