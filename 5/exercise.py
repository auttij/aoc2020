filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def get_ids(arr):
	ids = []
	for line in arr:
		lo = 0
		hi = 127
		for char in line[:7]:
			if char == 'B':
				lo = int((lo + hi)/2 + 1)
			elif char == 'F':
				hi = int((lo + hi)/2)
		row = lo

		lo = 0
		hi = 7
		three = []
		for char in line[-3:]:
			three.append(char)
			if char == 'R':
				lo = int((lo + hi)/2 + 1)
			elif char == 'L':
				hi = int((lo + hi)/2)
		column = lo
		ids.append(row * 8 + column)
	return ids

def exercise1(arr):
	ids = get_ids(arr)
	return max(ids)


def exercise2(arr):
	ids = get_ids(arr)
	s = sorted(ids)
	previous = s[0]
	for id in s[1:]:
		if id != previous + 1:
			return previous + 1
		previous = id
	pass

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
