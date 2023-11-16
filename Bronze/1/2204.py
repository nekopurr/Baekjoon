# https://www.acmicpc.net/problem/2204

while True:
    t = int(input())
    if t == 0:
        break

    dic = []
    lower_dic = []
    for _ in range(t):
        dic.append(input())

    for word in dic:
        lower_dic.append(word.lower())

    a = lower_dic.index(min(lower_dic))
    print(dic[a])