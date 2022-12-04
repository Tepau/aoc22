def parse_file(file):
	with open(file) as f:
		data = [x for x in f.read().splitlines()]

		return data


def part_one(data):
	count = 0
	for d in data:
		new_d = d.split(',')
		x0, x1  = new_d[0].split('-')
		y0, y1  = new_d[1].split('-') 
		x0, x1, y0, y1 = int(x0), int(x1), int(y0), int(y1)

		if (y0 >= x0 and y1 <= x1)  or (x0 >= y0 and x1 <= y1) :
			count += 1

	return count 


def part_two(data):
	count = 0
	for d in data:
		new_d = d.split(',')
		x0, x1  = new_d[0].split('-')
		y0, y1  = new_d[1].split('-') 
		x0, x1, y0, y1 = int(x0), int(x1), int(y0), int(y1)
		range1 = range(x0, x1+1)
		range2 = range(y0, y1+1)
	
		if len(set(range1).intersection(set(range2))) > 0:
			count += 1

	return count



x = parse_file('../data/day4.txt')
print('Part one : ', part_one(x))
print('Part two : ', part_two(x))



