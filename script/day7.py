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
            r_d['/'.join(path)].append(folder)
        if command[0].isdigit():
            r_d['/'.join(path)].append(int(command.split()[0]))    
    
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
                        dict_tree[k][idx] =  get_folder_size(dict_tree, key=k+'/'+val)
    
    else:
        selected_key = dict_tree[key]
        if all(isinstance(y, int) for y in selected_key):
                dict_tree[key] = [sum(dict_tree[key])]
        else:
            for idx, val in enumerate(selected_key):
                if type(val) == str:
                    dict_tree[key][idx] =  get_folder_size(dict_tree, key=key+'/'+val)
        return sum(selected_key)
                                        
    return dict_tree


def part_one(all_folder_size):
    sum_part_1 = 0
    for path in folders_size:
        if sum(path) <= 100000:
            sum_part_1 += sum(path)
    return sum_part_1


def part_two(all_folder_size, total_size):
    result_list = []
    for path in folders_size:
        if total_size - sum(path) <= 40000000:
            result_list.append(sum(path))
    
    return min(result_list)
        

data = parse_file('../data/day7.txt')
clean_path = clean_path_and_content(data)
folders_size = get_folder_size(clean_path).values()
sum_all_file = sum(clean_path['/'])

print('PART 1 : ',part_one(folders_size))
print('PART 2 : ', part_two(folders_size, sum_all_file))