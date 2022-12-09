import pprint
import pdb

with open('../data/day8.txt') as f:
    data = [list(x) for x in f.read().splitlines()]


len_data = len(data[0])
height = len(data)

coordinate_with_edge = []
coordinate_without_edge = []

for i in range(len_data):
    for y in range(len_data):
        coordinate_with_edge.append((i,y))

for i in range(1, len_data-1):
    for y in range(1,len_data-1):
        coordinate_without_edge.append((i,y))

def check(list1, val):
    return(all(x < val for x in list1))


count = 0
for coord in coordinate_without_edge:
        x ,y = coord
        nb = int(data[x][y])
        top = []
        bottom = []
        left = []
        right = []
        for c in coordinate_with_edge:
            a,b = c
            if a == x and b < y:
                left.append(int(data[a][b]))
            if a == x and b > y:
                right.append(int(data[a][b]))
            if a < x and b == y:
                top.append(int(data[a][b]))
            if a > x and b == y:
                bottom.append(int(data[a][b]))
        
        for direction in [top, bottom, left, right]:
            if check(direction, nb):
                count += 1
                break
    

edge = height * 2 + len_data * 2 - 4
print('PART1 : ',count+edge)

my_list = []
def my_funct(nb_to_compare, nb_list):
    for idx, nb in enumerate(nb_list):
        if nb >= nb_to_compare:
            return idx + 1
    
    return len(nb_list)


for coord in coordinate_without_edge:
        x ,y = coord
        nb = int(data[x][y])
        before_mult = 1
        top = []
        bottom = []
        left = []
        right = []
        for c in coordinate_with_edge:
            a,b = c
            if a == x and b < y:
                left.append(int(data[a][b]))
            if a == x and b > y:
                right.append(int(data[a][b]))
            if a < x and b == y:
                top.append(int(data[a][b]))
            if a > x and b == y:
                bottom.append(int(data[a][b]))
        
        for direction in [top[::-1], bottom, left[::-1], right]:
            nb_to_mult = my_funct(nb, direction)
            if nb_to_mult > 0:
                before_mult *= nb_to_mult
            
        my_list.append(before_mult)
              
print('PART 2 : ', max(my_list))
