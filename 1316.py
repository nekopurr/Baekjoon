# https://www.acmicpc.net/problem/1316

N = int(input())
answer = 0

for _ in range(N):
    word = input()
    check = 0
    for w in range(len(word) - 1):
        if word[w] != word[w+1]:
            new_word = word[w+1:]
            if new_word.count(word[w]):
                check += 1
    if check == 0:
        answer += 1

print(answer)