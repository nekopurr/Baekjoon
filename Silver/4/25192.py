# https://www.acmicpc.net/problem/25192

N = int(input())
answer = 0
log = set()

for _ in range(N):
    chat = input()

    if chat != 'ENTER':
        if chat not in log:
            log.add(chat)
            answer += 1
    elif chat == 'ENTER':
        log.clear()

print(answer)