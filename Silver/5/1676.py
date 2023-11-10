import math

N = int(input())
fac_N = str(math.factorial(N))
answer = 0

for i in range(1, len(fac_N) + 1):
    if fac_N[len(fac_N) - i] == '0':
        answer += 1
    else:
        break

print(answer)