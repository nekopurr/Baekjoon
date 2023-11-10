# https://www.acmicpc.net/problem/1427

N = int(input())
print(int(''.join(sorted(str(N), reverse=True))))