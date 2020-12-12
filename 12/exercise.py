import math

filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def move(lon, lat, dir, dist):
	if dir == "E":
		lon +=  dist
	elif dir == "W":
		lon -= dist
	elif dir == "N":
		lat += dist
	elif dir == "S":
		lat -= dist 
	return [lon, lat]

def moving(lon, lat, face, dir, dist):
	a = ["N", "E", "S", "W"]
	if dir in a:
		lon, lat = move(lon, lat, dir, dist)
	elif dir == "F":
		lon, lat = move(lon, lat, face, dist)
	else:
		steps = int(dist / 90)
		ind = a.index(face)
		if dir == "R":
			face = a[(ind + steps) % 4]
		elif dir == "L":
			face = a[(ind - steps) % 4]

	return [lon, lat, face]

def exercise1(input):
	face = "E"
	lon = 0
	lat = 0

	for line in input:
		dir = line[0]
		dist = int(line[1:])
		lon, lat, face = moving(lon, lat, face, dir, dist)
	return abs(lon) + abs(lat)



def navigate(lon, lat, dir, dist):
	a = ["N", "E", "S", "W"]
	mlon = 0
	mlat = 0
	if dir in a:
		lon, lat = move(lon, lat, dir, dist)
	elif dir == "F":
		mlon = lon * dist
		mlat = lat * dist
	else: 
		steps = int(dist / 90)
		if steps == 2:
			lon = -lon
			lat = -lat
		elif (steps == 1 and dir == "R") or (steps == 3 and dir == "L"):
			temp = lon
			lon = lat
			lat = -temp
		elif (steps == 1 and dir == "L") or (steps == 3 and dir == "R"):
			temp = lat
			lat = lon
			lon = -temp
	return [lon, lat, mlon, mlat]

def exercise2(input):
	lon = 10
	lat = 1
	movelon = 0
	movelat = 0

	for line in input:
		dir = line[0]
		dist = int(line[1:])
		lon, lat, mlon, mlat = navigate(lon, lat, dir, dist)
		movelon += mlon
		movelat += mlat
	return abs(movelon) + abs(movelat) 

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr)
	print(result)
	result = exercise2(arr)
	print(result)
