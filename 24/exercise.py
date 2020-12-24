import itertools
filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

opp = { "e": "w", "w": "e", "se" : "nw", "nw": "se", "sw": "ne", "ne": "sw"}

def shorten(t):
	for val in t:
		if opp[val] in t:
			t.remove(val)
			t.remove(opp[val])
	return t

def lf(t):
	x, y = 0, 0
	for d in t:
		if d == "e":
			x += 1
		if d == "w":
			x -= 1
		if d == "ne":
			x += 0.5
			y += 0.5
		if d == "se":
			x += 0.5
			y -= 0.5
		if d == "sw":
			x -= 0.5
			y -= 0.5
		if d == "nw":
			x -= 0.5
			y += 0.5
	return f"x{x} y{y}"

def nei(t):
	x, y = t.split()
	x, y = float(x[1:]), float(y[1:])
	l =	[(1,0), (-1,0)] + [p for p in itertools.product([0.5, -0.5], repeat=2)]
	return	[f"x{x+xi} y{y+yi}" for xi, yi in l]

def exercise1(arr):
	tilesdir = {}
	tiles = []
	for line in arr:
		l = list(line)
		
		t = []
		c = ""
		i = 0
		while i < len(l):
			v = l[i]
			c += v
			if "e" == v or "w" == v:
				t.append(c)
				c = "" 
			i += 1
		tiles.append(t)

	for tile in tiles:
		loc = lf(tile)
		if loc not in tilesdir:
			tilesdir[loc] = "black"
		else:
			if tilesdir[loc] == "black":
				tilesdir[loc] = "white"
			else:
				tilesdir[loc] = "black"    

	count = 0
	fc = 0
	for t in tilesdir:
		if tilesdir[t] == "black":
			count += 1
		fc += 1
	return count


def exercise2(arr):
	
	tilesdir = {}
	tiles = []
	for line in arr:
		l = list(line)
		
		t = []
		c = ""
		i = 0
		while i < len(l):
			v = l[i]
			c += v
			if "e" == v or "w" == v:
				t.append(c)
				c = "" 
			i += 1
		tiles.append(t)

	for tile in tiles:
		# ts = shorten(tile)
		loc = lf(tile)
		# print(loc)
		# print(nei(loc))
		if loc not in tilesdir:
			tilesdir[loc] = "black"
		else:
			if tilesdir[loc] == "black":
				tilesdir[loc] = "white"
			else:
				tilesdir[loc] = "black"

	day = 1

	tmpdir = {}
	while day <= 100:
		keys = list(tilesdir.keys())
		for key in keys:
			ns = nei(key)
			for n in ns:
				if n not in tilesdir:
					tilesdir[n] = "white"
		for tile in tilesdir:
			val = tilesdir[tile]
			ns = nei(tile)
			nvals = [tilesdir[n] if n in tilesdir else "white" for n in ns]
			bcount = nvals.count("black")
			if val == "black":
				if bcount == 0 or bcount > 2:
					tmpdir[tile] = "white"
				else:
					tmpdir[tile] = "black"
			else:
				if bcount == 2:
					tmpdir[tile] = "black"
				else:
					tmpdir[tile] = "white"
		for tile in tmpdir:
			tilesdir[tile] = tmpdir[tile]
			# tmpdir[tile] = "white"

		
		count = 0
		for t in tilesdir:
			if tilesdir[t] == "black":
				count += 1
		print(f"Day {day}: {count}")
		day += 1
	return count

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)

