filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def read_tiles(arr):
	tiles = {}
	tile = []
	i = 0
	tilenum = 0
	while i < len(arr):
		line = arr[i]
		if "Tile" in line:
			tilenum = line.split()[1][:-1]
		elif not line:
			tiles[tilenum] = tile
			tile = []
		else: 
			tile.append(line)
		i += 1
	tiles[tilenum] = tile
	tile = []
	return tiles

def get_tile_edges(arr):
	edges = []
	edges.append(arr[0])
	edges.append(arr[-1])
	ew = edges.append("".join([i[0] for i in arr]))
	ee = edges.append("".join([i[-1] for i in arr]))
	return edges

def flip_horizontal(arr):
	return [i[::-1] for i in arr]

def flip_vertical(arr):
	return arr[::-1]

def trim_edges(arr):
	return [i[1:-1] for i in arr[1:-1]]

def solve_puzzle(neighbors, puzzle, size):
	corners = []
	edges = []
	middle = []

	for tile in neighbors:
		nei = neighbors[tile]
		if len(nei) == 2:
			corners.append(tile)
		elif len(nei) == 3:
			edges.append(tile)
		else:
			middle.append(tile)

def exercise1(tiles):
	tile_edges = {}
	for tile in tiles:
		tile_edges[tile] = get_tile_edges(tiles[tile])

	reverse_tile_edges = {}
	for tile in tile_edges:
		edges = tile_edges[tile]
		for edge in edges:
			rev = edge[::-1]
			if edge not in reverse_tile_edges:
				reverse_tile_edges[edge] = [tile]
			else:
				reverse_tile_edges[edge].append(tile)
			if rev not in reverse_tile_edges:
				reverse_tile_edges[rev] = [tile]
			else:
				reverse_tile_edges[rev].append(tile)

	neighbors = {}
	for tile in tile_edges:
		neighbors[tile] = set()
	for tile in tile_edges:
		edges = tile_edges[tile]
		for edge in edges:
			nei = reverse_tile_edges[edge]
			if len(nei) != 1:
				neighbors[nei[0]].add(nei[1])
				neighbors[nei[1]].add(nei[0])

	sum = 1
	for tile in neighbors:
		nei = neighbors[tile]
		if len(nei) < 3:
			sum *= int(tile)
	return sum

def exercise2(tiles):
	pass

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	tiles = read_tiles(arr)
	result = exercise1(tiles.copy())
	print(result)
	result = exercise2(tiles.copy())
	print(result)

