#j178. 手遊廣告 (Advertisement)
a,b = map(int,input().split())
mons = list(map(int, input().split()))

for i in range(a):
    if mons[i] >= b:
        print(b)
        break
    b += int(mons[i])
else:
    print(b)
