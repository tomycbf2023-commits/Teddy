#k254. 拍七 (Seven)
def haveb(i,b): # 若 i 內出現 b 則回傳 T 否則回傳 F
    s = str(i)
    for a in s:
        if int(a) == b:
            return True
    return False

s,e,b,k = map(int,input().split())
p = 0 # 拍手次數
for i in range(s,e+1):
    if i%b==0 or haveb(i,b):
        p += 1
        if p == k :
            print(i)
            break
if p != k:
    print(-1)
