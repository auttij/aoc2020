filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def readCards(arr):
	cards = []
	l = []
	for line in arr[1:]:
		if line == "":
			pass
		elif "Player" in line:
			cards.append(l)
			l = []
		else:
			l.append(int(line))
	cards.append(l)
	return cards

def comp(a, b):
	if a > b:
		return [a, b], []
	else:
		return [], [b, a]

def exercise1(arr):
	c1, c2 = readCards(arr)
	while len(c1) > 0 and len(c2) > 0:
		a, b = c1.pop(0), c2.pop(0)
		ao, bo = comp(a, b)
		c1 = c1 + ao
		c2 = c2 + bo

	winner = []
	if (len(c1) > 0):
		winner = c1 
	else:
		winner = c2

	sum = 0
	for i, val in enumerate(winner[::-1]):
		sum += (i+1) * val
	return sum

# create a string representation of a game state for easy comparing
def fingerprint(c1, c2):
	return "a" + "".join([str(i) for i in c1]) + "b" + "".join([str(i) for i in c2])

def rgame(c1, c2):
	prev_games = []
	while len(c1) > 0 and len(c2) > 0:
		ap, bp = c1[0], c2[0]
		f = fingerprint(c1, c2)
		if f in prev_games:
			return c1 + c2, []
		prev_games.append(f)
		if len(c1) > ap and len(c2) > bp:
			c1r, c2r = c1[1:ap + 1], c2[1:bp + 1]
			aro, bro = rgame(c1r, c2r)
			ao, bo = a, b = c1.pop(0), c2.pop(0)
			if len(aro) > len(bro):
				c1 = c1 + [a, b]
			else:
				c2 = c2 + [b, a]
		else:
			a, b = c1.pop(0), c2.pop(0)
			ao, bo = comp(a, b)
			c1 = c1 + ao
			c2 = c2 + bo
	return c1, c2

def exercise2(arr):
	c1, c2 = readCards(arr)
	c1, c2 = rgame(c1, c2)
	
	winner = []
	if (len(c1) > 0):
		winner = c1 
	else:
		winner = c2

	sum = 0
	for i, val in enumerate(winner[::-1]):
		sum += (i+1) * val
	return sum

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)

