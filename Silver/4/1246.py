# https://www.acmicpc.net/problem/1246

N, M = map(int, input().split())
P = sorted([int(input()) for _ in range(M)])

max_profit, best_price = 0, 0

for i in range(M):
    if M - i <= N:
        profit = P[i] * (M - i)
    else:
        profit = N

    if max_profit < profit:
        max_profit = profit
        best_price = P[i]

print(best_price, max_profit)