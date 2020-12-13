import operator

filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def exercise1(arr):
	time = int(arr[0])
	schedule = arr[1]
	buses = []
	for bus in schedule.split(","):
		if bus != "x":
			buses.append(int(bus))

	t = time
	etimes = []
	for bus in buses:
		over = t % bus
		etimes.append(time + bus - over)
	earliest = min(etimes)
	ebus = buses[etimes.index(earliest)]
	return ebus * (earliest - time)


	return earliest

def inv(a, m) : 
	m0 = m 
	x0 = 0
	x1 = 1

	if (m == 1): 
		return 0

	# Apply extended Euclid Algorithm 
	while (a > 1) : 
		# q is quotient 
		q = a // m 

		t = m 

		# m is remainder now, process  
		# same as euclid's algo 
		m = a % m 
		a = t 

		t = x0 

		x0 = x1 - q * x0 

		x1 = t 
		
	# Make x1 positive 
	if (x1 < 0) : 
		x1 = x1 + m0 

	return x1

def findMinX(num, rem, k) : 
	prod = 1
	for i in range(0, k) : 
		prod = prod * num[i] 
	result = 0
	for i in range(0,k): 
		pp = prod // num[i] 
		result = result + rem[i] * inv(pp, num[i]) * pp 
	return result % prod

def exercise2(arr):
	time = int(arr[0])
	schedule = arr[1]

	num = []
	rem = []
	xcounter = 0
	for i, bus in enumerate(schedule.split(",")):
		if bus != "x":
			num.append(int(bus))
			rem.append((int(bus) - xcounter) % int(bus))
		xcounter += 1

	res = findMinX(num, rem, len(num))
	return res

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)

