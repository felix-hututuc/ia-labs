from copy import deepcopy
import re


def read_instance(path):
    n = 0
    blocks = []
    with open(path, 'r') as f:
        input = f.readline()
        n = int(input.split(' ')[-1])
        input = f.readline()
        result = re.findall(r'(\d+, \d+)', input)
        blocks += [[int(block.split(', ')[0]), int(block.split(', ')[1])] for block in result]
    return n, blocks


def calculate_domains(domains, last_place):
    temp_domains = deepcopy(domains)
    for queen_id in range(len(domains)):
        for position in domains[queen_id]:
            if position == last_place[1] \
               or abs(position - last_place[1]) == abs(queen_id - last_place[0]):
                temp_domains[queen_id].remove(position)
        if len(temp_domains[queen_id]) == 0:
            return False
    return temp_domains


def solve_n_queens(domains):
    n = len(domains)
    positions = [-1 for _ in range(n)]
    queen = 0
    index = 0
    while index < len(domains[queen]):
        positions[queen] = domains[queen][index]
        temp_domains = calculate_domains(domains, (queen, domains[queen][index]))
        if not temp_domains:
            index += 1
        else:
            domains = temp_domains
            if -1 in positions:
                mrv = min([len(domains[i]) for i in range(n) if positions[i] == -1])
            else:
                break
            for i in range(n):
                if len(domains[i]) == mrv and positions[i] == -1:
                    queen = i
                    break
            index = 0
    return positions


def blocked_queens(n, blocks):
    domains = [[i + 1 for i in range(n)] for j in range(n)]
    for pair in blocks:
        domains[pair[0] - 1].remove(pair[1])
    print(domains)
    positions = solve_n_queens(domains)
    print(positions)


# n, blocks = read_instance("E:\\Facultate\\Informatica_2020\\Semestrul_5\\IA\\block-10-36-2.param")
n = 8
blocks = []
blocked_queens(n, blocks)
