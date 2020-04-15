import board
import time
from Allan import Allan
from Barry import Barry

board.printBoard()
allan = Allan(1)
board.printBoard()
barry = Barry(2)
time.sleep(1)
while board.checkIfWin != True:
	barry.makeMove()
	board.printBoard()
	time.sleep(1)
	allan.makeMove()
	board.printBoard()
	time.sleep(1)
	if board.isFull():
		board.clear()
		board.printBoard()


board.printBoard()
print("Game Over")
