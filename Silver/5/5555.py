# https://www.acmicpc.net/problem/5555

word = input()
testcase = int(input())
answer = 0

for _ in range(testcase):
    ring = input() * 2
    if word in ring:
        answer += 1

print(answer)