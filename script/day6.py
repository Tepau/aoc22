def parse_file(file):
    with open(file) as f:
        data = f.read()
        return data


def resolution(data, nb):
    for i in range(len(data)):
        l = [data[i] for i in range(i, i+nb)]
        if len(l) == len(set(l)):
            return i+nb


x = parse_file('../data/day6.txt')

print('Part one : ', resolution(x,4))
print('Part two : ', resolution(x,14))