filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def exercise1(arr):
	arr = read_file_to_arr(filepath)
	own = "shiny gold bag"
	dir = {}
	
	for line in arr:
		out, inList = line[:-1].split(" contain ")
		ins = inList.split(", ")
		names = [''.join([i for i in s if not i.isdigit()]) for s in ins]
		stripped = [item.strip() for item in names]
		for i, bag in enumerate(stripped):
			if bag[-1] != 's':
				bag += "s"
				stripped[i] = bag
		dir[out] = stripped

	togold = - 1
	for key in dir.keys():
		result = dfs(dir, key)
		togold += result

	return togold

def dfs(dir, key):
	own = "shiny gold bags"
	end = "no other bags"

	stack = []
	stack.append(key)
	seen = [key]
	while (len(stack)):
		s = stack[-1]
		stack.pop()
		# print("key", s)

		if s == own:
			return 1
		elif s == "no other bags":
			pass
		else:
			for val in dir[s]:
				if val not in seen:
					stack.append(val)
	return 0


def exercise2(arr):
	arr = read_file_to_arr(filepath)
	own = "shiny gold bags"
	end = "no other bags"
	dir = {}
	
	for line in arr:
		out, inList = line[:-1].split(" contain ")
		ins = inList.split(", ")
		stripped = [item.strip() for item in ins]
		for i, bag in enumerate(stripped):
			if bag[-1] != 's':
				bag += "s"
				stripped[i] = bag
		dir[out] = stripped
	
	result = dfsrec(dir, own, 1)
	return result - 1

def dfsrec(dir, key, num):
	end = "no other bags"
	if end in dir[key]:
		return num
	else: 
		vals = dir[key]
		out = []
		for val in vals:
			if val[0].isdigit():
				i = int(val[0])
				s = val[2:]
				result = dfsrec(dir, s, i)
			else: 
				result = dfsrec(dir, val, 0)
			out.append(result)
		return num + num * sum(out)

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
