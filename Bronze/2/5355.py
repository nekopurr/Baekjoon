# https://www.acmicpc.net/problem/5355

T = int(input())

for testcase in range(T):
    formula = list(input().split())
    n = float(formula[0])

    for i in range(1, len(formula)):
        if formula[i] == '@':
            n *= 3
        elif formula[i] == '%':
            n += 5
        elif formula[i] == '#':
            n -= 7

    print(f'{n:.2f}')