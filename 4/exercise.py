import re

filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def intersect(nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: List[int]
	"""
	m = {}
	if len(nums1)<len(nums2):
		nums1,nums2 = nums2,nums1
	for i in nums1:
		if i not in m:
			m[i] = 1
		else:
			m[i]+=1
	result = []
	for i in nums2:
		if i in m and m[i]:
			m[i]-=1
			result.append(i)
	return result


def exercise1(arr):
	fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	pps = []
	pp = []
	for line in arr:
		if line == "":
			flat_list = [item for sublist in pp for item in sublist]
			pps.append(flat_list)
			pp = []
		else:
			pp.append(line.split())

	legit = 0
	for passport in pps:
		keys = [i.split(":")[0] for i in passport]
		found = intersect(keys, fields)
		if len(found) == 7:
			legit +=1

	return legit
	

def exercise2(arr):
	fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	pps = []
	pp = []
	for line in arr:
		if line == "":
			flat_list = [item for sublist in pp for item in sublist]
			pps.append(flat_list)
			pp = []
		else:
			pp.append(line.split())
	flat_list = [item for sublist in pp for item in sublist]
	pps.append(flat_list)

	legit = 0
	for passport in pps:
		broken = False
		dir = {}
		for val in passport:
			key, value = val.split(":")
			dir[key] = value
		for field in fields:
			if field not in dir:
				broken = True
				break
		if broken:
			continue

		eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

		if int(dir["byr"]) < 1920 or int(dir["byr"]) > 2002 or len(dir["byr"]) != 4 or not dir["byr"].isdecimal():
			continue
		if int(dir["iyr"]) < 2010 or int(dir["iyr"]) > 2020 or len(dir["byr"]) != 4 or not dir["byr"].isdecimal():
			continue
		if int(dir["eyr"]) < 2020 or int(dir["eyr"]) > 2030:
			continue
		if "cm" in dir["hgt"]:
			if int(dir["hgt"].split("cm")[0]) < 150 or int(dir["hgt"].split("cm")[0]) > 193:
				continue
		elif "in" in dir["hgt"]:
			if int(dir["hgt"].split("in")[0]) < 59 or int(dir["hgt"].split("in")[0]) > 76:
				continue
		else:
			continue
		if dir["ecl"] not in eyes:
			continue
		if len(dir["pid"]) > 9 or len(dir["pid"]) < 9 or not dir["pid"].isdecimal():
			continue
		match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', dir["hcl"])
		if not match:
			continue
		legit +=1
		
	return legit

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
