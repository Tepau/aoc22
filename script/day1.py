def parse_file(file_name):
	with open(file_name) as f:
		data = [l for l in f.read().splitlines()]
		return data

def part_one(data):
	r_v = 0
	passage = 0
	for d in data:
		try:
			d = int(d)
			passage += int(d)
		except ValueError:
			if passage > r_v:
				r_v = passage
			passage = 0
	return r_v


def part_two(data):
	passage = 0
	keep = []
	for d in data:
		try:
			d = int(d)
			passage += d
		except ValueError:
			keep.append(passage)
			passage = 0
	return sum(sorted(keep)[-3:])

	

data = parse_file('../data/day1.txt')
print(part_one(data))
print(part_two(data))
