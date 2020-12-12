filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def exercise1(arr):
	width = len(arr[0])
	x = 0
	trees = 0
	
	for line in arr:
		if line[x] == "#":
			trees += 1
		x = (x+3) % width
	return trees

def exercise2(arr):
	width = len(arr[0])
	steps = [[1,1], [3, 1], [5, 1], [7, 1], [1, 2]]
	res = []
	for xstep, ystep in steps:
		x = 0
		trees = 0
		for y, line in enumerate(arr):
			if not y % ystep == 0:
				continue
			if line[x] == "#":
				trees += 1
			x = (x + xstep) % width
		res.append(trees)
	return min(res)

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)

