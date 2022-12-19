def parse_file(file) -> list :
    with open(file) as f:
        data = [x.split() for x in f.read().splitlines()]
        return data


def adapt_position(position_head: tuple, position_tail: tuple) -> tuple :
    '''
        Fonction qui adapte la position de la queue en fonction de la position de la tête
        À appeler à chaque déplacement
    '''
    x_head, y_head = position_head
    x_tail, y_tail = position_tail
  
    if x_head == x_tail: # même ligne
        if y_head < y_tail:
            y_tail = y_head + 1
        if y_head > y_tail:
            y_tail = y_head - 1
    
    if y_head == y_tail: #même colonne
        if x_head < x_tail:
            x_tail = x_head + 1
        if x_head > x_tail:
            x_tail = x_head - 1

    else: #Diagonale
        if not (x_head in (range(x_tail-1, x_tail+2)) and y_head in (range(y_tail-1, y_tail+2))):

            if x_head > x_tail:
                x_tail = x_tail + 1
            elif  x_head < x_tail: 
                x_tail = x_tail -1 

            if y_head > y_tail:
                y_tail = y_tail + 1
            elif  y_head < y_tail: 
                y_tail = y_tail -1 

    return x_tail, y_tail

def manage_direction(h_p, t_p, nb, direction=None, positions=None):
    all_tail_position = []
  
    if direction is not None:
        if direction == 'R':
            for i in range(nb):
                t_p = adapt_position((h_p[0], h_p[1] + i + 1), t_p)
                all_tail_position.append(t_p)
            h_p = (h_p[0], h_p[1] + nb)
            
        elif direction == 'L':
            for i in range(nb):
                t_p = adapt_position((h_p[0], h_p[1] - (i + 1) ), t_p)
                all_tail_position.append(t_p)
            h_p = (h_p[0], h_p[1] - nb)

        elif direction == 'D':
            for i in range(nb):
                t_p = adapt_position((h_p[0] - (i + 1), h_p[1]), t_p)
                all_tail_position.append(t_p)
            h_p = (h_p[0] - nb , h_p[1])

        elif direction == 'U':
            for i in range(nb):
                t_p = adapt_position((h_p[0] + i + 1, h_p[1]), t_p)
                all_tail_position.append(t_p)
            h_p = (h_p[0] + nb , h_p[1])
    
    elif positions is not None:
        for p in positions:
            t_p = adapt_position(p, t_p)
            all_tail_position.append(t_p)

    return h_p, t_p, all_tail_position

def part_one(data):
    tail_positions = []
    h_p = (0,0)
    t_p = (0,0)
    for line in data:
       direction, nb = line
       nb = int(nb)
       h_p, t_p, all_tail_position = manage_direction(h_p, t_p, nb, direction)
       tail_positions += all_tail_position

    return tail_positions


def part_two(data):
    positions = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    r_v = []
    for line in data:
        direction, nb = line
        nb = int(nb)
        for idx, p in enumerate(positions):
            if idx < len(positions)-1:
                lead_position = p
                follow_position = positions[idx + 1]
                if idx == 0:
                    new_lead_position, new_follow_position, all_pos = manage_direction(lead_position, follow_position, nb, direction=direction)
                else: 
                    new_lead_position, new_follow_position, all_pos = manage_direction(
                        h_p = lead_position,
                        t_p = follow_position,
                        nb =nb,
                        positions = all_position_visited,)
                
                all_position_visited = [x for x in all_pos]
                positions[idx] = new_lead_position
                positions[idx+1] = new_follow_position

                if idx == 8:
                    r_v += [x for x in all_pos]
    
    return r_v 
        
data = parse_file('../data/day9.txt')
print('PART 1 : ',len(set(part_one(data))))
print('PART 2 : ', len(set(part_two(data))))
