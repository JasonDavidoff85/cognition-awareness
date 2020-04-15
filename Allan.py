import board
import random

class Allan:
	def __init__(self, value):
		self.value = value
		if board.isEmpty():
			board.move((1,1),self.value)
		# self.makeMove()

	def makeMove(self):
		bestMoves = set([])
		nextBest = set([])
		leastBest = set([])
		for x in range(0,3):
			for y in range(0,3):
				if (board.isOpen((x,y)) == False):
					#print(x,y,"is not open")
					for adjacent in board.getPerimiter((x,y)):
						if board.getValue((x,y)) == board.getValue(adjacent):
							print("Found two next to each other:",(x,y),adjacent)
							bestSpace = self.getRemainingSpace((x,y),adjacent)
							if board.isValidMove(bestSpace):
								bestMoves.add(bestSpace)
					for gap in board.getGaps((x,y)):
						if board.getValue((x,y)) == board.getValue(gap):
							print("Found gap:", (x,y), gap)
							bestSpace = self.getRemainingSpace((x,y),gap)
							if board.isValidMove(bestSpace):
								bestMoves.add(bestSpace)
				if (board.isOpen((x,y)) == False) and (board.getValue((x,y)) == self.value):
					for adjacent in board.getPerimiter((x,y)):
						if board.getValue(adjacent) == 0:
							nextBest.add(adjacent)
				if board.isOpen((x,y)):
					leastBest.add((x,y))

		print("best:",bestMoves)
		print("next best:",nextBest,"\n")
		#print("least best:",leastBest)
		bestMoves = list(bestMoves)
		nextBest = list(nextBest)
		leastBest = list(leastBest)

		if len(bestMoves) == 0 and len(nextBest) == 0:
			board.move(random.choice(leastBest), self.value)
		elif len(bestMoves) == 0:
			board.move(random.choice(nextBest), self.value)
		elif len(bestMoves) > 0:
			board.move(random.choice(bestMoves), self.value)
		else:
			print("Boards full!")


	def getRemainingSpace(self,coord1,coord2):
		values = (0,1,2)
		if coord1[1] == coord2[1]:
			for i in values:
				if i not in (coord1[0],coord2[0]):
					return (i,coord1[1])
		elif coord1[0] == coord2[0]:
			for i in values:
				if i not in (coord1[1],coord2[1]):
					return (coord1[0],i)
		else:
			for i in values:
				if i not in (coord1[0], coord2[0]):
					return (i,i)


