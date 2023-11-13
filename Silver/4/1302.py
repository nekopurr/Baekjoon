# https://www.acmicpc.net/problem/1302

N = int(input())
seller = {}

for b in range(N):
    book = input()
    if book not in seller:
        seller[book] = 1
    else:
        seller[book] += 1

best_seller = []

for key, value in seller.items():
    if value == max(seller.values()):
        best_seller.append(key)

print(sorted(best_seller)[0])