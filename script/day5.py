import collections

def parse_file(file):
    with open(file) as f:
        data = [x for x in f.read().splitlines()]
        idx_nb = data.index("") - 1
        idx_ins = data.index("") + 1
        cleaned_number = clean_number(data[:idx_nb])
        cleaned_instruction = clean_instruction(data[idx_ins:])
        return cleaned_number, cleaned_instruction


def clean_number(data):
    r_d = {}
    for y in data:
        for i in range(0, len(y)):
            if y[i].isalpha():
                idx = int(i/4) + 1
                if idx in r_d:
                    r_d[idx] += [y[i]]
                else:
                    r_d[idx] = [y[i]]

    return r_d

def clean_instruction(data):
    r_d = []
    for line in data: 
        l = [int(x) for x in line.split() if x.isdigit()]
        r_d.append(l)

    return r_d

def resolution(col_num, instructions, part=1):
    r_v = ''
    for ins in instructions:
        list_num = col_num[ins[1]]
        to_remove_and_add = list_num[0:ins[0]]
        if part == 1:
            col_num[ins[2]] = to_remove_and_add[::-1] + col_num[ins[2]]
            col_num[ins[1]] = list_num[ins[0]:]

        if part == 2:    
            col_num[ins[2]] = to_remove_and_add + col_num[ins[2]]
            col_num[ins[1]] = list_num[ins[0]:]


    od = collections.OrderedDict(sorted(col_num.items()))
    for k, v in od.items():
        r_v += v[0]

    return r_v



number_clean, instruction_clean = parse_file('../data/day5.txt')
print(resolution(number_clean, instruction_clean, part=1))
print(resolution(number_clean, instruction_clean, part=2))