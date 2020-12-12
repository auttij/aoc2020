import functools
import numpy as np
import itertools
from typing import Callable, List, Tuple

filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def neighbors(a, radius, rowNumber, columnNumber):
	return [[a[i][j] if  i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) and not (i+1 == rowNumber and j+1 == columnNumber) else 0
		for j in range(columnNumber-1-radius, columnNumber+radius)]
			for i in range(rowNumber-1-radius, rowNumber+radius)]

def prettyprint(arr):
	print("------------------")
	for line in arr:
		print("".join(line))
	print("------------------")

def copy(orig, cop):
	for i, line in enumerate(orig):
		cop[i] = list(orig[i])

def equal(a, b):
	if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, a, b), True) :  
		return True
	else : 
		return False

def deepcount(arr, char):
	c = 0
	for line in arr:
		c += line.count(char)
	return c

def exercise1(arr):
	nextarr = []
	lastarr = []
	for i, line in enumerate(arr):
		arr[i] = list(line)
		nextarr.append(["."]*len(line))
		lastarr.append(["#"]*len(line))
	
	loops = 0
	while not equal(lastarr, nextarr):
		copy(arr, lastarr)
		for y, row in enumerate(arr):
			for x, char in enumerate(row):
				if char != ".":
					nei = neighbors(arr, 1, y+1, x+1)
					flatlist = [item for sublist in nei for item in sublist if item != 0]
					taken = flatlist.count("#")
					if char == "L" and taken == 0:
						nextarr[y][x] = "#"
					elif char == "#" and taken >= 4:
						nextarr[y][x] = "L"
					else:
						nextarr[y][x] = arr[y][x]
		copy(nextarr, arr)
		loops += 1
	return deepcount(nextarr, "#")

def find_visible_target(matrix: Tuple[Tuple[str]], x: int, y: int, search_distance: int, stopper: Callable[[List[str]], bool] = lambda _: False) -> bool:
	visible = []
	for xo, yo in itertools.product((-1, 0, 1), repeat=2):
		if xo == yo == 0:
			continue

		for i in range(1, search_distance + 1):
			nx = x + (i * xo)
			ny = y + (i * yo)
			if nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[x]):
				break

			current = matrix[nx][ny]
			if current == '.':
				continue
			visible += current
			if stopper(visible):
				return True
			break

	return False

def process_matrix(matrix, search_distance, occ_empty_max):
	return tuple(
		tuple(
			('L' if find_visible_target(
				matrix, x, y, search_distance,
				(lambda visible: '#' in visible)
				if current == 'L' else
				(lambda visible: visible.count('#') == occ_empty_max)
			) else '#') if current != '.' else '.'
			for y, current in enumerate(row)
		)
		for x, row in enumerate(matrix)
	)

def solve(arr, search_distance, occ_empty_max) -> int:
	matrix = tuple(map(tuple, arr))

	while True:
		new_matrix = process_matrix(matrix, search_distance, occ_empty_max)
		if new_matrix == matrix:
			break
		matrix = new_matrix

	return sum(row.count('#') for row in matrix)

def exercise2(arr):
	return solve(arr, max(len(arr), len(arr[0])), 5)

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
