filepath = "input.txt"

def read_file_to_arr(filepath):
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def intersect(lists):
	l = lists[0]
	for li in lists:
		l = list(set(l) & set(li))
	return l

def diff(list1, list2):
	return list(set(list1) - set(list2))

def exercise1(arr):
	ingredients = []
	allergens = []
	for i, line in enumerate(arr):
		ingr, alle = line.split(" (contains ")
		ingredients.append(ingr.split())
		allergens.append(alle[:-1].split(", "))

	# unique allergens	
	ui = list(set([i for sublist in ingredients for i in sublist]))
	ua = list(set([i for sublist in allergens for i in sublist]))
	pa = set()
	for a in ua:
		foods = []
		for i, al in enumerate(allergens):
			if a in al:
				foods.append(ingredients[i])
		inter = intersect(foods)
		for f in inter:
			pa.add(f)

	unall = diff(ui, pa)

	count = 0
	for i in ingredients:
		for j in i:
			if j in unall:
				count += 1
	return count


def exercise2(arr):
	ingredients = []
	allergens = []
	for i, line in enumerate(arr):
		ingr, alle = line.split(" (contains ")
		ingredients.append(ingr.split())
		allergens.append(alle[:-1].split(", "))

	# unique allergens	
	ui = list(set([i for sublist in ingredients for i in sublist]))
	ua = list(set([i for sublist in allergens for i in sublist]))
	pa = set()
	for a in ua:
		foods = []
		for i, al in enumerate(allergens):
			if a in al:
				foods.append(ingredients[i])
		inter = intersect(foods)
		for f in inter:
			pa.add(f)

	unall = diff(ui, pa)
	fi = []
	ar = {}
	for a in ua:
		ar[a] = []
	for i, ing in enumerate(ingredients):
		food = []
		for j in ing:
			if j not in unall:
				food.append(j)
		al = allergens[i]
		for a in al:
			ar[a].append(food)
		fi.append(food)

	for a in ar:
		ar[a] = intersect(ar[a])

	finished = False
	seen = {}
	while finished == False:
		finished = True
		for a in ar:
			if len(ar[a]) > 1:
				finished = False
			elif a not in seen:
				seen[a] = True
				for al in ar:
					if al != a:
						ar[al] = diff(ar[al], ar[a])

	out = ",".join([ar[i][0] for i in sorted(ar.keys())])
	return out

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = exercise1(arr.copy())
	print(result)
	result = exercise2(arr.copy())
	print(result)

