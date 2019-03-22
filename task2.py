class Matrix:

	def __init__(self, matrix):
		self.matrix = matrix

	def add(self, another_matrix):
		if len(self.matrix) == len(another_matrix):
			added_matrix = []
			for idx, value in enumerate(self.matrix):
				added_matrix.append(self.matrix[idx] + another_matrix[idx])
			print("first matrix", self.matrix)
			print("second matrix", another_matrix)
			print("added matrix", added_matrix)

	def multiply(self, another_matrix):
		first = self.matrix[0]*another_matrix[0] + self.matrix[1]*another_matrix[2]
		second = self.matrix[0]*another_matrix[1] + self.matrix[1]*another_matrix[3]
		third = self.matrix[0]*another_matrix[1] + self.matrix[1]*another_matrix[3]
		fourth = self.matrix[0]*another_matrix[1] + self.matrix[1]*another_matrix[3]

matrix1 = Matrix([1,4,3,2])
matrix1.add([1,5,68,8])	

matrix2 = Matrix([4,6,8,7])
matrix2.add(4,6,86,6)				
		
