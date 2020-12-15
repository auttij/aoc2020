filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def memGameHelper(arr, goal):
	res = {}
	i = 0
	num = 0
	for j, x in enumerate(arr):
		res[int(x)] = j
		if j == len(arr) - 1:
			i = j
			num = int(x)

	prev = 0
	while i < goal:
		if num not in res:
			prev = num
			res[num] = i
			num = 0
		else:
			prev = num
			num = i - res[num]
			res[prev] = i
		i += 1
	return prev

def exercise1(arr):
	return memGameHelper(arr, 2020)


def exercise2(arr):
	return memGameHelper(arr, 30000000)

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)

