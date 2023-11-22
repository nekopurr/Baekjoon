# https://www.acmicpc.net/problem/1076

resistance = [
    'black', 'brown', 'red', 'orange', 'yellow',
    'green', 'blue', 'violet', 'grey', 'white'
]

a, b, c = [input() for _ in range(3)]
answer = ((resistance.index(a) * 10) + resistance.index(b)) * 10 ** resistance.index(c)
print(answer)