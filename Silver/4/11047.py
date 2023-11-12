# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())
coin = []
answer = 0

for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

for c in coin:
    if c > K:
        pass
    else:
        n = K // c
        K -= c * n
        answer += n

print(answer)