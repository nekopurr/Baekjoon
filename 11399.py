# https://www.acmicpc.net/problem/11399

N = int(input())
P = list(map(int, input().split()))

P.sort()
delay = 0
answer = 0

for i in P:
    delay += i
    answer += delay

print(answer)