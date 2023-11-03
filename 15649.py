# https://www.acmicpc.net/problem/15649

from itertools import permutations

N, M = map(int, input().split())
num_list = [i for i in range(1, N + 1)]

sequence = list(permutations(num_list, M))

for i in sequence:
    print(' '.join(map(str, i)))