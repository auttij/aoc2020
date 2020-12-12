filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def exercise1(arr):
	ints = [int(i) for i in arr]
	sor = sorted(ints)

	previous = sor[0]
	ones = 1
	threes = 1
	for val in 	sor[1:]:
		diff = val - previous
		if diff == 1:
			ones += 1
		if diff == 3:
			threes	+= 1
		previous = val

	return ones * threes
	

def exercise2(arr):
	arr = read_file_to_arr(filepath)
	ints = [int(i) for i in arr]
	ints.append(0)
	m = max(ints)
	ints.append(m+3)
	sor = sorted(ints)
	

	chains = []
	chain = []
	for i in sor:
		if len(chain) == 0:
			chain.append(i)
		elif i - chain[-1] == 1:
			chain.append(i)
		else:
			chains.append(chain)
			chain = [i]

	multips = [1, 1, 1, 2, 4, 7, 13, 24, 44, 81]
	cm = []
	for chain in chains:
		cm.append(multips[len(chain)])
	
	sum = 1
	for i in cm:
		sum = sum * i
	return sum


def next(arr, val, i):
	out = []
	if i + 1 < len(arr) and arr[i+1] - val <= 3:
		out.append(i+1)
	if i + 2 < len(arr) and arr[i+2] - val <= 3:
		out.append(i+2)
	if i + 3 < len(arr) and arr[i+3] - val <= 3:
		out.append(i+3)
	mapped = [arr[i] for i in out]
	return out


if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
