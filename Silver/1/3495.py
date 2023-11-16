# https://www.acmicpc.net/problem/3495

h, w = map(int, input().split())
area = [list(input()) for _ in range(h)]
answer = 0

for i in range(h):
    slash = 0
    for j in area[i]:
        if j == '/' or j == '\\':
            slash += 1
        if slash % 2 == 1 and j == '.':
            answer += 1
    answer += (slash // 2)

print(answer)