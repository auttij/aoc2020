import itertools
import copy

ACTIVE = '#'
INACTIVE = '.'
filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def prettyprint(arr):
	for line in arr:
		for row in line:
			print("".join(row))
		print("----------")
	print("==================")

def neighbours(arr, x, y, z):
	out = []
	for k in range(-1, 2):
		for  j in range(-1, 2):
			for i in range(-1, 2):
				if z+k >= 0 and z+k < 23 and y+j >= 0 and y+j < 23 and x+i >= 0 and x+i < 23:
					if not (i == 0 and j == 0 and k ==0):
						out.append(arr[z+k][y+j][x+i])
	return out

def neighbours4d(arr, x, y, z, f):
	out = []
	r = range(-1, 2)
	for l in r:
		for k in r:
			for j in r:
				for i in r:
					if l+f >= 0 and l+f <= 23\
						and z+k >= 0 and z+k <= 23\
						and y+j >= 0 and y+j <= 23\
						and x+i >= 0 and x+i <= 23:
						if not (i == 0 and j == 0 and k == 0 and l == 0):
							out.append(arr[l+f][z+k][y+j][x+i])
	return out


def exercise1(arr):
	# Initialize grid
	grid = [[['.' for _ in range(24)] for _ in range(24)] for _ in range(24)]
	for ix, i in enumerate(arr):
		for jx, j in enumerate(i):
			grid[12][ix+9][jx+9] = j

	# 6 cycles
	for _ in range(6):
		grid_clone = copy.deepcopy(grid)
		for i in range(24):
			for j in range(24):
				for k in range(24):
					nei = neighbours(grid, k, j, i)
					count_active = nei.count(ACTIVE)

					if (grid[i][j][k] == ACTIVE) and (not(2 <= count_active <= 3)):
						grid_clone[i][j][k] = INACTIVE

					if (grid[i][j][k] == INACTIVE) and (count_active == 3):
						grid_clone[i][j][k] = ACTIVE
		grid = grid_clone

	# Count active cubes for result
	active = 0
	for i in range(24):
		for j in range(24):
			for k in range(24):
				if grid[i][j][k] == ACTIVE:
					active += 1
	return active

def exercise2(arr):
	# Initialize grid
	grid = [[[['.' for _ in range(24)] for _ in range(24)] for _ in range(24)] for _ in range(24)]
	for ix, i in enumerate(arr):
		for jx, j in enumerate(i):
			grid[12][12][ix+9][jx+9] = j

	# Run 6 cycles
	for _ in range(6):
		grid_clone = copy.deepcopy(grid)
		for i in range(24):
			for j in range(24):
				for k in range(24):
					for l in range(24):
						nei = neighbours4d(grid, l, k, j, i)
						count_active = nei.count(ACTIVE)
						if (grid[i][j][k][l] == ACTIVE) and not(2 <= count_active <= 3):
							grid_clone[i][j][k][l] = INACTIVE

						if (grid[i][j][k][l] == INACTIVE) and (count_active == 3):
							grid_clone[i][j][k][l] = ACTIVE
		grid = grid_clone

	# Count active cubes
	active = 0
	for i in range(24):
		for j in range(24):
			for k in range(24):
				for l in range(24):
					if grid[i][j][k][l] == ACTIVE:
						active += 1
	return active

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)