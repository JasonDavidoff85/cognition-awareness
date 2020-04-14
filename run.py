import board
from Allan import Allan

myValue = 2
allan = Allan(1)
while board.isFull() != True:
	board.printBoard()
	x = int(input("x: "))
	y = int(input("y: "))
	board.move((x,y), myValue)
	allan.makeMove()

board.printBoard()
print("Game Over")
