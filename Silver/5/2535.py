# https://www.acmicpc.net/problem/2535

N = int(input())
data = []

for i in range(N):
    country, student, score = map(int, input().split())
    data.append([country, student, score])

data.sort(key = lambda x:x[2], reverse=True)

answer = []
count = {}

for row in data:
    key = row[0]
    if key not in count:
        count[key] = 1
        answer.append(row)
    elif count[key] < 2:
        count[key] += 1
        answer.append(row)

for row in answer[:3]:
    print(f'{row[0]} {row[1]}')