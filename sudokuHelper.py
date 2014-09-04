import sys

class SudokuHelper:
	def __init__(self):
		self.digits = range(1, 10)
		self.grid = self.createGrid()

	def createGrid(self):
		grid = {}

		for i in range(0, 10):
			grid[i] = self.createSquare()

		return grid

	def createSquare(self):
		# Initialize empty square
		square = {}

		# Populate square with each digit corresponding to an empty list
		for digit in self.digits:
			square[digit-1] = 0

		# Return template
		return square

	def displayGrid(self):
		for row in self.grid:
			output = ""
			for col in self.grid[row]:
				val = self.grid[row][col]
				if val == 0:
					output += "- "
				else:
					output += "%s ", val
			print(output)

sh = SudokuHelper()
sh.displayGrid()