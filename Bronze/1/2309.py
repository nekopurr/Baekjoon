# https://www.acmicpc.net/problem/2309

from itertools import combinations

dwarf = [int(input()) for _ in range(9)]

for i in combinations(dwarf, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break