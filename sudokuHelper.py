import sys

class SudokuHelper:
	def __init__(self):
		self.range = range(0, 9)
		self.numbers = range(1, 10)
		self.grid = self.loadGrid()

	def createGrid(self):
		grid = {}

		for i in self.range:
			grid[i] = self.createRow()

		return grid

	def createRow(self):
		# Initialize empty row
		row = {}

		# Populate row
		for col in self.range:
			row[col] = 0

		# Return template
		return row

	def loadGrid(self):
		# Use hard-coded grid for now
		grid = {}
		grid[0] = {1: 0, 2: 6, 3: 2, 4: 0, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0}
		grid[1] = {1: 1, 2: 0, 3: 3, 4: 2, 5: 0, 6: 9, 7: 5, 8: 0, 9: 4}
		grid[2] = {1: 0, 2: 8, 3: 0, 4: 6, 5: 0, 6: 7, 7: 0, 8: 2, 9: 3}
		grid[3] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 4, 7: 0, 8: 5, 9: 0}
		grid[4] = {1: 3, 2: 0, 3: 6, 4: 0, 5: 0, 6: 0, 7: 8, 8: 0, 9: 9}
		grid[5] = {1: 0, 2: 9, 3: 0, 4: 8, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
		grid[6] = {1: 6, 2: 5, 3: 0, 4: 7, 5: 0, 6: 3, 7: 0, 8: 9, 9: 0}
		grid[7] = {1: 2, 2: 0, 3: 4, 4: 9, 5: 0, 6: 1, 7: 6, 8: 0, 9: 7}
		grid[8] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 6, 6: 0, 7: 2, 8: 3, 9: 0}

		return grid;


	def displayGrid(self):
		for row in self.grid:
			output = ""
			for col in self.grid[row]:
				val = self.grid[row][col]
				if val == 0:
					output += "  "
				else:
					output += "%s " % val
			print(output)

	def searchSquare(self, squareId):
		possibilities = {}
		repeat = false
		numbers = self.getSquare(squareId);
		missingNumbers = self.getMissingNumbers(numbers);

		for cell in square:
			rowNumbers = self.getNumbersFromRow(cell, square);

	def getSquare(self, squareId):
		return 1;

	def getNumbersFromRow(self, row):
		numbers = []
		values = self.grid[row].values()
		for val in values:
			if val > 0:
				numbers.append(val)
		return numbers

	def getNumbersFromCol(self, col):
		numbers = []
		for i in self.range:
			val = self.grid[i][col]
			if val > 0:
				numbers.append(val)
		return numbers

	def getMissingNumbers(self, numbers):
		missingValues = []
		for i in self.numbers:
			if i not in numbers:
				missingValues.append(i);
		return missingValues

sh = SudokuHelper()
sh.displayGrid()
numbers = sh.getNumbersFromRow(1)
print (numbers)
print (sh.getMissingNumbers(numbers))
print("Getting numbers from col 0")
colNumbers = sh.getNumbersFromCol(1)
print(colNumbers)
print (sh.getMissingNumbers(colNumbers))