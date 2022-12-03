def parse_file(file):
	with open(file) as f:
		data = [x for x in f.read().splitlines()]

		return data

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def common_elements(list1, list2, list3=None):
	for element in list1:
		if list3 is not None:
			if element in list2 and element in list3:
				return element
		else:
		 	if element in list2:
		 		return element

def part_one(data):
	same_elements = []
	for e in data:
		l1 = e[:int(len(e)/2)]
		l2 = e[int(len(e)/2):]
		same_elements.append(common_elements(l1, l2))

	return same_elements


def part_two(data):
	same_elements = []
	group_by = []
	for x in range(0,len(data),3):
		group_by.append(data[x:x+3])

	for g in group_by:
		same_elements.append(common_elements(g[0], g[1], g[2]))

	return same_elements


def get_value(element_list):
	r_v = 0
	for e in element_list:
		idx = ALPHABET.find(e.lower()) + 1
		if e.isupper():
			idx += 26
		r_v += idx

	return r_v

x = parse_file('../data/day3.txt')

print('PART 1 : ', get_value(part_one(x)))
print('PART 2 : ', get_value(part_two(x)))