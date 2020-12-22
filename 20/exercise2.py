from collections import deque
import regex as re

filepath = "input.txt"

NESW = ["N", "E", "S", "W"]
NDIR = { "N": 0, "E": 1, "S": 2, "W": 3 }

class Tile(object):
	def __init__(self, id, st):
		self.id = id
		self.st = st
		self.nei = [None, None, None, None]
		self.neiCount = 0

	#starting north and going clockwise
	def edges(self):
		return [self.st[0], "".join([i[-1] for i in self.st]), self.st[-1], "".join([i[0] for i in self.st])]
	
	def flip_horizontal(self):
		self.st = [i[::-1] for i in self.st]
		self.nei[1], self.nei[3] = self.nei[3], self.nei[1]
	def flip_vertical(self):
		self.st =  self.st[::-1]
		self.nei[0], self.nei[2] = self.nei[2], self.nei[0]
	def no_edges(self):
		return [i[1:-1] for i in self.st[1:-1]]
	def __str__(self):
		return self.id + "\n" + "\n".join(self.no_edges())
	def __repr__(self):
		return "T" + self.id
	def set_neighbor(self, d, other):
		self.nei[NESW.index(d)] = other
	def edge_matching(self, d, other):
		return self.edges()[NDIR[d]] == other.edges()[NDIR[d]-2]
	def get_dir_of_edge(self, edge):
		if edge in self.edges():
			return NESW[self.edges().index(edge)]
		else:
			return NESW[self.edges().index(edge[::-1])]
	def edge_by_dir(self, dir):
		return self.edges()[NDIR[dir]]
	def rot90(self):
		self.st = ["".join(list(reversed(col))) for col in zip(*self.st)]


def rot90(s):
	return ["".join(list(reversed(col))) for col in zip(*s)]

def transform(p):
	for _ in range(4):
		yield p
		yield '\n'.join(l[::-1] for l in p.split('\n')) # flip
		p = '\n'.join(''.join(l[::-1]) for l in zip(*p.split('\n'))) # rotate

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def read_tiles(arr):
	tiles = []
	tile = []
	i = 0
	tilenum = 0
	while i < len(arr):
		line = arr[i]
		if "Tile" in line:
			tilenum = line.split()[1][:-1]
		elif not line:
			t = Tile(tilenum, tile)
			tiles.append(t)
			tile = []
		else: 
			tile.append(line)
		i += 1
	t = Tile(tilenum, tile)
	tiles.append(t)
	return tiles

def exercise2(tiles):
	tiledir = {}
	revedges = {}
	nei = {}
	for tile in tiles:
		tiledir[tile.id] = tile
		nei[tile.id] = []
		for edge in tile.edges():
			rev = edge[::-1]
			if edge not in revedges:
				revedges[edge] = [tile]
			else:
				revedges[edge].append(tile)
			if rev not in revedges:
				revedges[rev] = [tile]
			else:
				revedges[rev].append(tile)

	for edge in list(revedges.keys())[::2]:
		t = revedges[edge]
		if len(t) == 2:
			for i, tile in enumerate(t):
				tile.neiCount += 1
				nei[t[i].id].append(t[i-1].id)
	stack = []
	start = None
	for tile in nei:
		if len(nei[tile]) == 2:
			stack.append(tiledir[tile])
			start = tiledir[tile]
			break
	
	sides = []
	for e in stack[0].edges():
		if len(revedges[e]) > 1:
			sides.append(e)
	for s in sides:
		d = stack[0].get_dir_of_edge(s)
		if d == "N":
			stack[0].flip_vertical()
		elif d == "W":
			stack[0].flip_horizontal()

	seen = [stack[0]]
	while len(stack) > 0:
		t = stack[-1]
		n = nei[stack[-1].id]
		e = [i for i in revedges[t.edge_by_dir("E")] if i.id != t.id]
		s = [i for i in revedges[t.edge_by_dir("S")] if i.id != t.id]

		if len(e) > 0:
			t.set_neighbor("E", e[0])
		if len(s) > 0:
			t.set_neighbor("S", s[0])

		if len(e) > 0 and e[0] not in seen:
			t2 = e[0]
			d = t2.get_dir_of_edge(t.edge_by_dir("E"))
			if d == "N" or d == "S":
				t2.rot90()
			d = t2.get_dir_of_edge(t.edge_by_dir("E"))
			if d == "E":
				t2.flip_horizontal()
			if not t.edge_matching("E", t2):
				t2.flip_vertical()
			stack.append(t2)
			seen.append(t2)
		else:
			stack.pop()
			if len(stack) == 0:
				if len(s) > 0 and s[0] not in seen:
					t2 = s[0]
					d = t2.get_dir_of_edge(t.edge_by_dir("S"))
					if d == "W" or d == "E":
						t2.rot90()
					d = t2.get_dir_of_edge(t.edge_by_dir("S"))
					if d == "S":
						t2.flip_vertical()
					if not t.edge_matching("S", t2):
						t2.flip_horizontal()
					stack.append(t2)
					seen.append(t2)

	puzzle = []
	row = []
	stack = [start]
	seen = []
	while len(stack) > 0:
		t = stack[-1]
		n = t.nei		
		
		if t not in seen:
			seen.append(t)
			row.append(t.id)

		if n[NDIR["E"]] != None and n[NDIR["E"]] not in seen:
			t2 = n[NDIR["E"]]
			stack.append(t2)
			seen.append(t2)
			row.append(t2.id)
		else:
			stack.pop()
			if len(stack) == 0:	
				if n[NDIR["S"]] != None and n[NDIR["S"]] not in seen:
					t2 = n[NDIR["S"]]
					stack.append(t2)
					seen.append(t2)
					puzzle.append(row)
					row = [t2.id]
	puzzle.append(row)
	out = []
	ls = ["" for i in range(8)]
	for row in puzzle:
		for tid in row:
			for i, s in enumerate(tiledir[tid].no_edges()):
				ls[i] = ls[i] + s
		out += ls
		ls = ["" for i in range(8)]
	
	image = "\n".join(out)
	print(image)

	spacing = '[.#\n]{77}'
	monster = f'#.{spacing+"#....#"*3}##{spacing}.#{"..#"*5}'
	
	for image_t in transform(image):
		m = len(re.findall(monster, image_t, overlapped=True))
		if m:
			return sum(c == '#' for c in image_t) - 15*m
			print('Part 2:', sum(c == '#' for c in image_t) - 15*m)
			break

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	tiles = read_tiles(arr)
	result = exercise2(tiles)
	print(result)