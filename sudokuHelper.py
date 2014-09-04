import sys

class SudokuHelper:
	def __init__(self):
		self.gridSize = range(0, 9)
		self.counter = 1
		self.grid = self.createGrid()

	def createGrid(self):
		grid = {}

		for i in self.gridSize:
			grid[i] = self.createRow()

		return grid

	def createRow(self):
		# Initialize empty row
		row = {}

		# Populate row
		for col in self.gridSize:
			row[col] = self.counter
			self.counter += 1

		# Return template
		return row

	def displayGrid(self):
		for row in self.grid:
			output = ""
			for col in self.grid[row]:
				val = self.grid[row][col]
				if val == 0:
					output += "- "
				else:
					output += "%s " % val
			print(output)

sh = SudokuHelper()
sh.displayGrid()