import itertools

filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def band(mask, num):
	numpad = num.zfill(36)
	out = list(mask)
	for i, x in enumerate(out):
		if x == "X":
			out[i] = numpad[i]
	return "".join(out)


def exercise1(arr):
	mask = ""
	res = {}

	for line in arr:
		id, val = line.split(" = ")
		if id == "mask":
			mask = val
		else:
			pos = id.split("[")[1].split("]")[0]
			bin = "{0:b}".format(int(val))
			out = band(mask, bin)
			res[pos] = int(out, 2)

	sum = 0
	for key in res.keys():
		sum += res[key]
	return sum

def perms(elements,n):
    return permutations_helper(elements,[0]*n,n-1)#this is generator

def permutations_helper(elements,result_list,d):
    if d<0:
        yield tuple(result_list)
    else:
        for i in elements:
            result_list[d]=i
            all_permutations = permutations_helper(elements,result_list,d-1)#this is generator
            for g in all_permutations:
                yield g

def floatpos(address):
	out = []
	num = address.count("X")
	com = perms(["0","1"], num)
	ps = ["".join(c) for c in com]
	for perm in ps:
		bin = address
		for i in perm:
			bin = bin.replace("X", i, 1)
		out.append(int(bin, 2))
	return out

def band2(mask, num):
	numpad = num.zfill(36)
	out = list(mask)
	for i, x in enumerate(numpad):
		if x == "1" and out[i] != "X":
			out[i] = numpad[i]
	return "".join(out)

def exercise2(arr):
	mask = ""
	res = {}

	for line in arr:
		id, val = line.split(" = ")
		if id == "mask":
			mask = val
		else:
			pos = id.split("[")[1].split("]")[0]
			bin = "{0:b}".format(int(pos)).zfill(36)
			address = band2(mask, bin)
			addresses = floatpos(address)
			for a in addresses:
				res[a] = int(val)

	sum = 0
	for key in res.keys():
		sum += res[key]
	return sum

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)

