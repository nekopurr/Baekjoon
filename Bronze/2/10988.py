# https://www.acmicpc.net/problem/10988

word = list(str(input()))
print(1 if list(reversed(word)) == word else 0)