# https://www.acmicpc.net/problem/7785

n = int(input())
check = {}
log = []

for _ in range(n):
    a, b = input().split()
    check[a] = b

for a, b in check.items():
    if b == 'enter':
        log.append(a)

log.sort(reverse=True)

for employee in log:
    print(employee)


# remove의 시간복잡도는 O(N)이다.