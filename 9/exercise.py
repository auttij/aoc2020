filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(int(line.strip()))
	return arr

def exercise1(arr):
	preamblen = 25
	stack = arr[:preamblen]
	for i in arr[preamblen:]:
		boo = sumoftwo(stack, i)
		if boo:
			stack.append(i)
			stack = stack[1:]
		else:
			return i
	pass
	
def sumoftwo(arr, target):
	sor = sorted(arr)
	i = 0
	j = len(arr) - 1

	while i <= j:
		if sor[i] + sor[j] == target:
			return True
		elif sor[i] + sor[j] > target:
			j -= 1
		elif sor[i] + sor[j] < target:
			i += 1
	return False

def exercise2(arr):
	target = 393911906
	for i, val in enumerate(arr):
		sum = val
		subarr = [val]
		j = i+1
		while sum < target:
			nval = arr[j]
			subarr.append(nval)
			sum += nval
			j += 1
		if sum == target:
			mn = min(subarr)
			mx = max(subarr)
			return mn + mx


	pass

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
