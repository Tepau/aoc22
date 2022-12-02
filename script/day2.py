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

TEST = {
    1: ('A', 'X'), #Rock
    2: ('B', 'Y'), #Paper
    3: ('C', 'Z'), #Scissors
}

SCORES = {'win': 6, 'draw': 3, 'lost': 0}

def part_one(data):
    r_v = 0
    for t in data:
        adv, me = t
        r_v += VALUES[me]
        if VALUES[adv] == VALUES[me]:
            r_v += SCORES['draw']
        elif VALUES[adv] < VALUES[me]:
            if VALUES[adv] == 1:
                if VALUES[me] == 2:
                    r_v += SCORES['win']
                else:
                    r_v += SCORES['lost']
            else:
                r_v += SCORES['win']
        else:
            if VALUES[adv] == 3:
                if VALUES[me] == 2:
                    r_v += SCORES['lost']
                else:
                    r_v += SCORES['win']
            else:
                r_v += SCORES['lost']

    return r_v


def part_two(data):
    coresp = {
        'X': 'lost',
        'Y': 'draft',
        'Z': 'win'
    }
    r_v = []
    for d in data:
        adv, expected = d
        if coresp[expected] == 'draft':
            r_v.append((adv, adv))
        elif coresp[expected] == 'lost':
            if VALUES[adv] == 1:
                r_v.append((adv, 'Z'))
            elif VALUES[adv] == 2:
                r_v.append((adv, 'X'))
            else:
                r_v.append((adv, 'Y'))
        else:
            if VALUES[adv] == 1:
                r_v.append((adv, 'Y'))
            elif VALUES[adv] == 2:
                r_v.append((adv, 'Z'))
            else:
                r_v.append((adv, 'X'))
        
    print('r_v', r_v)
    return part_one(r_v)



x = parse_file('data/day2.txt')

print('Part one : ',part_one(x))
print('Part two : ',part_two(x))


