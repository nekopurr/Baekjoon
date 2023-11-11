# https://www.acmicpc.net/problem/1010
# 경우의 수 : nCr

import math

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    answer = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(answer)