#https://www.acmicpc.net/problem/5026

for i in range(int(input())):
    try:
        print(eval(input()))
    except:
        print("skipped")