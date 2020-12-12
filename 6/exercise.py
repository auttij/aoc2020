filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def letters(input):
	out = []
	for character in input:
		if character.isalpha():
			out.append(character)
	return ''.join(out)

def strIntersection(s1, s2):
	out = ""
	for c in s1:
		if c in s2 and not c in out:
			out += c
	return out

def exercise1(arr):
	arr.append("")
	groups = []
	group = []
	for line in arr:
		if line:
			legit = letters(line)
			group.append(legit)
		else:
			combined = "".join(group)
			unique = list(set(combined))
			groups.append(unique)
			group = []

	total = 0
	for group in groups:
		total += len(group)
	return total

def exercise2(arr):
	arr.append("")
	groups = []
	group = []
	for line in arr:
		if line:
			legit = letters(line)
			group.append(legit)
		else:
			intersect = ""
			if len(group) > 0:
				intersect = group[0]
				for string in group:
					intersect = strIntersection(intersect, string)
			unique = "".join(intersect)
			groups.append(unique)
			group = []

	total = 0
	for group in groups:
		total += len(group)

	return total

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)

