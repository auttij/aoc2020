import itertools

m = 20201227

def calc(s, p):
    ans = 0
    v = 1
    while v != p:
        ans += 1
        v = (s * v) % m

    return ans

def exercise1():
	# cp = 5764801
	# dp = 17807724
	cp = 6930903
	dp = 19716708
	rem = 20201227
	sub = 7

	# ls1 = calc(7, cp)
	# ls2 = calc(7, dp)
	# print(ls1, ls2)
	# print(pow(cp, ls1, m), pow(dp, ls2, m))

	for exponent in itertools.count():
		if pow(sub, exponent, m) == dp:
			return pow(cp, exponent, m)


def exercise2():
	pass

if __name__ == "__main__":
	print("part 1:")
	result = exercise1()
	print(result)
	print("part 2:")
	result = exercise2()
	print(result)

