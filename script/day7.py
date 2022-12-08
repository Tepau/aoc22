from collections import defaultdict


def parse_file(file):
    with open(file) as f:
        data = [x for x in f.read().splitlines()]
        return data


def clean_path_and_content(list_command):
    path = []
    r_d = defaultdict(list)
    for command in list_command:
        if command.startswith('$ cd'):
            rep = command.split()[-1]
            if rep == '..':
                path.pop()
            else:
                path.append(rep)
                
        if command.startswith('dir'):
            folder = command.split()[-1]
            r_d['$'.join(path)].append(folder)
        if command[0].isdigit():
            r_d['$'.join(path)].append(int(command.split()[0]))    
    
    return r_d


def get_folder_size(dict_tree, key=None):
    if key is None:
        for k,values in dict_tree.items():
            if all(isinstance(val, int) for val in values):
                dict_tree[k] = [sum(values)]
            else:
                for val in values:
                    if type(val) == str:
                        idx = values.index(val)
                        dict_tree[k][idx] =  get_folder_size(dict_tree, key=k+'$'+val)
    
    else:
        x = dict_tree[key]
        if all(isinstance(y, int) for y in x):
                dict_tree[key] = [sum(dict_tree[key])]
        else:
            for idx, val in enumerate(x):
                if type(val) == str:
                    dict_tree[key][idx] =  get_folder_size(dict_tree, key=key+'$'+val)
        return sum(x)
                                        
    return dict_tree


data = parse_file('../data/day7.txt')
clean_path = clean_path_and_content(data)
folders_size = get_folder_size(clean_path).values()
somme_part_1 = 0
for path in folders_size:
    if sum(path) <= 100000:
        somme_part_1 += sum(path)

print('PART 1 : ',somme_part_1)

somme_part_2 = sum(clean_path['/'])
result_list = []

for path in folders_size:
    if somme_part_2 - sum(path) <= 40000000:
        result_list.append(sum(path))

print('PART 2 : ', min(result_list) )