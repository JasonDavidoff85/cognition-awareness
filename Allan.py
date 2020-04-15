import board
import random

class Allan:
	def __init__(self, value):
		self.value = value
		if board.isEmpty():
			board.move((1,1),self.value)
		# self.makeMove()

	def makeMove(self):
		if board.isFull():
			return 0
		bestMoves = set([])
		nextBest = set([])
		okay = set([])
		leastBest = set([])
		for x in range(0,3):
			for y in range(0,3):
				if (board.isOpen((x,y)) == False):
					#print(x,y,"is not open")
					for adjacent in board.getPerimiter((x,y)):
						if board.getValue((x,y)) == board.getValue(adjacent):
							#print("Allan: Found two next to each other:",(x,y),adjacent)
							bestSpace = self.getRemainingSpace((x,y),adjacent)
							#print("Remian space:",bestSpace)
							if board.isValidMove(bestSpace):
								bestMoves.add(bestSpace)
					for gap in board.getGaps((x,y)):
						if board.getValue((x,y)) == board.getValue(gap):
							#print("Allan: Found gap:", (x,y), gap)
							bestSpace = self.getRemainingSpace((x,y),gap)
							if board.isValidMove(bestSpace):
								bestMoves.add(bestSpace)
				if (board.isOpen((x,y)) == False) and (board.getValue((x,y)) == self.value):
					for adjacent in board.getPerimiter((x,y)):
						if board.getValue(adjacent) == 0 and board.getValue(self.getRemainingSpace((x,y), adjacent)) == 0:
							nextBest.add(adjacent)
						elif board.getValue(adjacent) == 0:
							okay.add(adjacent)
				if board.isOpen((x,y)):
					leastBest.add((x,y))

		# print("Allan: best:",bestMoves)
		# print("Allan: next best:",nextBest)
		# print("Allan: okay:",okay)
		# print("Allan: least best:",leastBest)
		# print()
		bestMoves = list(bestMoves)
		nextBest = list(nextBest)
		okay = list(okay)
		leastBest = list(leastBest)

		if board.getValue((1,1)) == 0:
			board.move((1,1), self.value)
		elif len(bestMoves) == 0 and len(nextBest) == 0 and len(okay) == 0:
			reccomended = [i for i in leastBest if board.isCorner(i)]
			if len(reccomended) > 0:
				board.move(random.choice(reccomended), self.value)
			else:
				board.move(random.choice(leastBest), self.value)
		elif len(bestMoves) == 0 and len(nextBest) == 0:
			board.move(random.choice(okay), self.value)
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
		elif coord1[0] == coord1[1] and coord2[0] == coord2[1]:
			for i in values:
				if i not in (coord1[0], coord2[0]):
					return (i,i)
		elif coord1 == (1,1):
			return (coord2[1], coord2[0])
		elif coord2 == (1,1):
			return (coord1[1], coord1[0])
		else:
			return (1,1)


