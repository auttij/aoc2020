filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def exercise1(arr):
	results = []
	for line in arr:
		result = check_row1(line)
		results.append(result)
	return sum(results)

def exercise2(arr):
	results = []
	for line in arr:
		result = check_row2(line)
		results.append(result)
	return sum(results)

def check_row1(row):
	parts = row.split()
	low, high = [int(s) for s in parts[0].split("-") if s.isdigit()]
	char = parts[1][:-1]
	password = parts[2]
	count = password.count(char)
	if low <= count and count <= high:
		return 1
	else: 
		return 0


def check_row2(row):
	parts = row.split()
	low, high = [int(s) for s in parts[0].split("-") if s.isdigit()]
	char = parts[1][:-1]
	password = parts[2]
	txt = f"{password[low - 1]}{password[high - 1]}"
	if txt.count(char) == 1:
		return 1
	else:
		return 0



if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
