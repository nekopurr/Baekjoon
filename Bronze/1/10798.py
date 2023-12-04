# https://www.acmicpc.net/problem/10798

texts = []
length = []

for _ in range(5):
    text = input()
    texts.append(text)
    length.append(len(text))

for i in range(max(length)):
    for j in range(len(texts)):
        try:
            print(texts[j][i], end='')
        except IndexError:
            continue
