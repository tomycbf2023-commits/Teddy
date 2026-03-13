#k254. 拍七 (Seven)
s,e,b,k = map(int,input().split())
clap = 0
for i in range(s,e+1):
    if i % b == 0 or str(b) in set(str(i)):
        clap += 1
    if clap == k:
        res = i
        break
else:
    res = -1

print(res)
