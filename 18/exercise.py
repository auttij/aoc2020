import re

filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

class T:
	def __init__(self, v):
		self.v = v
	def __add__(self, other):
		return T(self.v + other.v)
	def __sub__(self, other):
		return T(self.v * other.v)
	def __mul__(self, other):
		return T(self.v + other.v)

def exercise1(arr):
	t = 0
	for line in arr:
		for d in range(10):
			line = line.replace(f"{d}", f"T({d})")
		line = line.replace("*", "-")
		t += eval(line, {"T": T}).v
	return(t)


def exercise2(arr):
	t = 0
	for line in arr:
		for d in range(10):
			line = line.replace(f"{d}", f"T({d})")
		line = line.replace("*", "-")
		line = line.replace("+", "*")
		t += eval(line, {"T": T}).v
	return(t)

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)

