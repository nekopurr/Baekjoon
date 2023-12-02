# https://www.acmicpc.net/problem/1037

N = int(input())
M = sorted(list(map(int, input().split())))
print(M[0] * M[-1])