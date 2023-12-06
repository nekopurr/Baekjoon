# https://www.acmicpc.net/problem/2941

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for i in range(len(croatia)):
    s = s.replace(croatia[i], '1')

print(len(s))