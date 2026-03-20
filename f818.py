n = int(input())
h = input().split() # 串列 文字
w = input().split() # 串列 文字
smallest = 1000000
for i in range (n):
    if int(h[i])*int(w[i]) < smallest:
        smallest = int(h[i])*int(w[i])
        kk=i # 代表乘積最小的索引值
print(h[kk],w[kk])    
