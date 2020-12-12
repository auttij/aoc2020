from itertools import combinations
from itertools import product
import numpy as np
import multiprocessing as mp
import random

filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(int(line.strip()))
	return arr

def write_arr_to_file(arr, filepath):
	with open(filepath, 'w') as f:
		for item in arr:
			f.write("%s\n" % item)

def exercise1(arr):
	sor = sorted(arr)
	i = 0
	j = len(sor) - 1
	goal = 2020

	while i <= j:
		if sor[i] + sor[j] == goal:
			return sor[i] * sor[j]
		elif sor[i] + sor[j] > goal:
			j -= 1
		elif sor[i] + sor[j] < goal:
			i += 1

def exercise2(arr):
	size = len(arr)
	goal = 2020
	for i in range(0, size-1): 
		s = set() 
		curr_sum = goal - arr[i] 
		for j in range(i + 1, size): 
			if (curr_sum - arr[j]) in s: 
				return (arr[j] * arr[i] * (curr_sum - arr[j]))
			s.add(arr[j]) 
	pass

def create_last_arrs():
	filename1 = "custom_expense_report.txt"
	filename2 = "custom_expense_report2.txt"
	arr = [] #read_file_to_arr() #sorted(read_file_to_arr())
	
	goal = 69420666
	start = -34710333

	curr = start

	top = len(arr) - 1
	results = []

	while len(results) < 30000:
		i = 0
		j = len(arr) - 1
		if curr > goal:
			print(f"finished at len {len(results)} curr: {curr}")
			break

		if curr > goal / 3:
			while i <= j:
				if arr[i] + arr[j] + curr  == goal:
					curr += random.randint(2000, 5000)
					break
				elif arr[i] + arr[j] + curr > goal:
					j -= 1
				elif arr[i] + arr[j] + curr < goal:
					i += 1
		else:
			i = 1
			j = 0
		if i > j:
			results.append(curr)
			arr.append(curr)
			curr += random.randint(1000, 5000)
		if len(results) % 2000 == 0:
			print(f"len results: {len(results)}, curr: {curr}")
		# else:
			# print(f"didn't work {arr[i]} + {arr[j]} + {curr} == {goal}")
			

	# print(results)
	write_arr_to_file(results, filename2)

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)
