filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def readInput(arr):
	seen = {}
	fields = {}
	mine = []
	tickets = []
	state = 0
	for line in arr:
		if len(line) > 0 and not line[0].isdigit():
			if line == "your ticket:":
				state = 1
			elif line == "nearby tickets:":
				state = 2
			else:
				name, spl = line.split(": ")
				ranges = spl.split(" or ")
				fields[name] = []
				for vals in ranges:
					bot, top = vals.split("-")
					fields[name].append(range(int(bot), int(top) + 1))
					for val in range(int(bot), int(top) + 1):
						seen[val] = True

		elif len(line) > 0 and line[0].isdigit():
			if state == 1:
				mine = [i for i in line.split(",")]
			elif state == 2:
				tickets.append([int(i) for i in line.split(",")])
	return [fields, mine, tickets, seen]

def exercise1(arr):
	fields, mine, tickets, seen = readInput(arr)
	
	error = 0
	for ticket in tickets:
		for val in ticket:
			if not val in seen.keys():
				error += val
	return error


def exercise2(arr):
	fields, mine, tickets, seen = readInput(arr)

	# List all the tickets that are valid
	valid = []
	for ticket in tickets:
		legit = True
		for val in ticket:
			if not val in seen.keys():
				legit = False
				continue
		if legit:
			valid.append(ticket)

	# Get all of the different fields that can be on different indexes
	fields_reverse = []
	for i, x in enumerate(mine):
		possible = []
		for ticket in valid:
			possible.append(ticket[i])
		possible_fields = []
		for field in fields:
			rl, rh = fields[field]
			works = True
			for val in possible:
				if not val in rl and not val in rh:
					works = False
			if works == True:
				possible_fields.append(field)
		fields_reverse.append(possible_fields)

	# filter out the the fields that can't be for different fields, because they're the only possibilities for another index
	all_clear = False
	i = 0
	seen = []
	while all_clear == False:
		all_clear = True
		for i in range(len(fields_reverse)):
			if len(fields_reverse[i]) != 1:
				all_clear = False
			elif len(fields_reverse[i]) == 1 and fields_reverse[i][0] not in seen:
				thing = fields_reverse[i][0]
				seen.append(fields_reverse[i][0])
				for j, field in enumerate(fields_reverse):
					if j != i:
						if thing in fields_reverse[j]: 
							fields_reverse[j].remove(thing)
	
	# calculate the product of ticket fields with "departure" on them from "my ticket"
	sum = 1
	for i, x in enumerate(fields_reverse):
		if "departure" in x[0]:
			sum *= int(mine[i])

	return sum

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)

