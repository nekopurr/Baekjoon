# https://www.acmicpc.net/problem/1236

N, M = map(int, input().split())
row_answer = 0
col_answer = 0
castle = []

for _ in range(N):
    castle.append(input())

for i in range(N):
    if 'X' not in castle[i]:
        row_answer += 1

for j in range(M):
    if 'X' not in [castle[i][j] for i in range(N)]:
        col_answer += 1

print(max(row_answer, col_answer))