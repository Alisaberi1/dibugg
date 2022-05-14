"""n = int(input())
a = input().split()
for i in a:
    t = int(i)
    if t <= 3:
        for j in range(t):
            print('*', end = '')
        print()
    else:
        print('*')"""
n = int(input())
a = input().split()
for i in a:
    t = int(i)
    if t <= 3:
      print(t*"*")
    else:
      print('*')
"""entery1 = int(input())
entery2 = list(map(int, input().split()))

for x in range(entery1):
    if entery2[x] <= 3:
        print("*"*entery2[x])"""

    else :print("*")
