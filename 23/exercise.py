filepath = "input.txt"

def read_file_to_arr(filepath):
	with open(filepath, 'r') as f:
		arr = f.read().strip()
	return arr


def game(cups, rounds):
	circle = dict(zip(cups, cups[1:] + cups[:1]))
	cv = cups[-1]

	for r in range(rounds):
		cv = circle[cv]

		pickup = list()
		tmp = cv
		for _ in range(3):
			tmp = circle[tmp]
			pickup.append(tmp)
		circle[cv] = circle[tmp]

		dv = cv - 1
		while dv in pickup or dv < 1:
			dv -= 1
			if dv < 1:
				dv = max(cups)

		circle[dv], circle[pickup[-1]] = pickup[0], circle[dv]
	return circle

def exercise1(arr):
	cups = list(map(int, arr))
	circle = game(cups, 100)

	next = circle[1]
	out = []
	while next != 1:
		out.append(next)
		next = circle[next]
	return "".join([str(i) for i in out])


def exercise2(arr):
	cups = list(map(int, arr))
	cups2 = cups + list(range(10, int(1e6) + 1))
	circle = game(cups2, int(1e7))
	ans = 1
	next_ = 1
	for _ in range(2):
		next_ = circle[next_]
		ans *= next_
	return ans

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr)
	print(result)
	result = exercise2(arr)
	print(result)

