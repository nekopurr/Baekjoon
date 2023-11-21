# https://www.acmicpc.net/problem/10093

a, b = map(int, input().split())

if a == b:
    print(0)

elif a > b:
    a, b = b, a
    answer = [str(i) for i in range(a + 1, b)]
    print(len(answer))
    print(' '.join(answer))

else:
    answer = [str(i) for i in range(a + 1, b)]
    print(len(answer))
    print(' '.join(answer))