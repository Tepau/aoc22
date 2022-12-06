def parse_file(file):
    with open(file) as f:
        data = [tuple(x.split()) for x in f.read().splitlines()]
        return data

VALUES = {
    'A': 1, #Rock
    'B': 2, #Paper
    'C': 3, #Scissors
    'X': 1, #Rock
    'Y': 2, #Paper
    'Z': 3, #Scissors
}

SCORES = {'win': 6, 'draw': 3, 'lost': 0}

# 1 beats 3 and loses 2, 2 beats 1 and loses 3, 3 beats 2 and loses 1
WIN_LOST = {
    1:(3,2), 2:(1,3), 3:(2,1)
}

def part_one(data):
    r_v = 0
    for t in data:
        adv, me = t
        r_v += VALUES[me]
        if VALUES[adv] == VALUES[me]:
            r_v += SCORES['draw']
        else:
            if WIN_LOST[VALUES[adv]][0] != VALUES[me]:
                 r_v += SCORES['win']
            else:
                 r_v += SCORES['lost']
    return r_v


def part_two(data):
    r_v = []
    for d in data:
        adv, expected = d
        if expected == 'Y':
            r_v.append((adv, adv))
        elif expected == 'X':
            keys = [k for k, v in VALUES.items() if v == WIN_LOST[VALUES[adv]][0]]
            r_v.append((adv, keys[1]))
        else:
            keys = [k for k, v in VALUES.items() if v == WIN_LOST[VALUES[adv]][1]]
            r_v.append((adv, keys[1]))
        
        
    return part_one(r_v)

x = parse_file('../data/day2.txt')

print('Part one : ',part_one(x))
print('Part two : ',part_two(x))


