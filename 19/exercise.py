import regex

filepath = "input.txt"

def defs(rules_s):
	for rule in rules_s.split('\n'):
		n,s = rule.split(': ',1)
		s = regex.sub(r'\s*(\d+)\s*',r'(?&r\1)',s)
		s = regex.sub(r'"(\w+)"',r'\1',s)
		yield "(?P<r{}>{})".format(n,s)

def exercise1(rules_s, messages_s):
	r=regex.compile(r'(?(DEFINE){})^(?&r0)$'.format(''.join(defs(rules_s))))
	return sum(1 if r.match(msg) else 0 for msg in messages_s.split('\n'))


def exercise2(rules_s, messages_s):
	rules_s = regex.sub(r'8: 42','8: 42 | 42 8',rules_s)
	rules_s = regex.sub(r'11: 42 31','11: 42 31 | 42 11 31',rules_s)
	r=regex.compile(r'(?(DEFINE){})^(?&r0)$'.format(''.join(defs(rules_s))))
	return sum(1 if r.match(msg) else 0 for msg in messages_s.split('\n'))

if __name__ == "__main__":
	rules_s, messages_s = open(filepath).read().split("\n\n",1)
	result = exercise1(rules_s, messages_s)
	print(result)
	result = exercise2(rules_s, messages_s)
	print(result)

# r=regex.compile(r'(?(DEFINE){})^(?&r0)$'.format(''.join(defs(rules_s))))
# print("part1:", sum(1 if r.match(msg) else 0 for msg in messages_s.split('\n')))
# rules_s, messages_s = open('./input.txt').read().split("\n\n",1)
# rules_s = regex.sub(r'8: 42','8: 42 | 42 8',rules_s)
# rules_s = regex.sub(r'11: 42 31','11: 42 31 | 42 11 31',rules_s)
# # .. or replace with what you had in the instructions page
# r=regex.compile(r'(?(DEFINE){})^(?&r0)$'.format(''.join(defs(rules_s))))
# print("part2:", sum(1 if r.match(msg) else 0 for msg in messages_s.split('\n')))