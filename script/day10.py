with open('../data/day10.txt') as f:
    data = []
    for line in f.read().splitlines():
        data += line.split() 

def part_one():
    stop_list = [20,60,100,140,180,220]
    sum_signal = 0
    nb_cycle = 0
    nb_x = 1
    for elt in data:
        nb_cycle += 1
        if nb_cycle in stop_list:
            sum_signal += nb_x * nb_cycle
        try:
            nb = int(elt)
            nb_x += nb
        except ValueError:
            pass
    return sum_signal

print('PART 1 : ', part_one())

def part_two():
    all_crt = []
    sprite_position = range(0,3)
    crt = ''
    stop_list = [0,40,80,120,160,200,239]
    nb_cycle = 0
    fake_cycle = 0
    nb_x = 1
    for elt in data:
        if nb_cycle in stop_list:
            all_crt.append(crt)
            crt = ''
            fake_cycle = 0
  
        if fake_cycle in sprite_position:
            crt += '#'
        else:
            crt += '.'

        try:
            nb = int(elt)
            nb_x += nb
            sprite_position = range(nb_x-1,nb_x+2)
        except ValueError:
            pass

        nb_cycle += 1
        fake_cycle += 1
            
    for x in all_crt:
        print(x)
