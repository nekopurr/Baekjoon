# https://www.acmicpc.net/problem/2738

N, M = map(int, input().split())
box1 = []
box2 = []

for i in range(N):
    i = list(map(int, input().split()))
    box1.append(i)

for i in range(N):
    i = list(map(int, input().split()))
    box2.append(i)

for i in range(N):
    for j in range(M):
        print(box1[i][j] + box2[i][j], end=' ')
    print()