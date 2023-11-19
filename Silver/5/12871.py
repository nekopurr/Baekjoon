# https://www.acmicpc.net/problem/12871

def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i


s = input().rstrip()
t = input().rstrip()
length = lcm(len(s), len(t))

if s * (length // len(s)) == t * (length // len(t)):
    print(1)
else:
    print(0)