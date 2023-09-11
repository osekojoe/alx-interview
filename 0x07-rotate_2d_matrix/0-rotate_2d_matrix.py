#!/usr/bin/python3


def rotate_2d_matrix(matrix):
	"""Rotate 2D Matrix"""
	n = len(matrix)

	# transpose matrix (swap rows with columns)
	for i in range(n):
		for j in range(i, n):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	# reverse each row
	for i in range(n):
		matrix[i].reverse()
