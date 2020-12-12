filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def exercise1(arr):
	accumulator = 0
	linenum = 0

	dir = {}

	for i, line in enumerate(arr):
		ins, num = line.split(" ")
		pos = num[0]
		numb = num[1:]
		dir[i] = [ins, int(numb), pos]

	seen = []
	top = 0
	while top not in seen or top == len(arr) - 1:
		seen.append(top)
		ins, num, pos = dir[top]
		if ins == "nop":
			top += 1
		if ins == "acc":
			if pos == "+":
				accumulator += num
			else:
				accumulator -= num
			top += 1
		if ins == "jmp":
			if pos == "+":
				top += num
			else:
				top -= num
	seen.append(top)
	return accumulator

def exercise2(arr):
	accumulator = 0
	linenum = 0

	dir = {}

	for i, line in enumerate(arr):
		ins, num = line.split(" ")
		pos = num[0]
		numb = num[1:]
		dir[i] = [ins, int(numb), pos]


	for key in dir.keys():
		topins, topnum, toppos = dir[key]
		if topins == 'acc': 
			continue
		else:
			if topins == 'jmp':
				dir[key][0] = 'nop'
			elif topins == 'nop':
				dir[key][0] = 'jmp'

			seen = []
			top = 0
			accumulator = 0
			while top not in seen and top < len(arr):
				seen.append(top)
				ins, num, pos = dir[top]
				if ins == "nop":
					top += 1
				if ins == "acc":
					if pos == "+":
						accumulator += num
					else:
						accumulator -= num
					top += 1
				if ins == "jmp":
					if pos == "+":
						top += num
					else:
						top -= num
			seen.append(top)
			if top >= len(arr) - 1:
				break
			if topins == 'jmp':
				dir[key][0] = 'jmp'
			elif topins == 'nop':
				dir[key][0] = 'nop'
	return accumulator

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
