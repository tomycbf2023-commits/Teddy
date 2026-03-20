n = int(input())    # 小雞總數量 轉成整數 n
c = input().split() # 小雞的編號 讀入 放到串列 c
e = input()         # 老鷹的編號 轉成整數
q = int(input())    # 幾回合
qc= input().split() # 每一回合抓到的小雞 放入串列 qc
for i in qc:        # 對於串列中的每一隻被抓到的小雞
    j = c.index(i)  # 找到 該小雞在原小雞串列c 的索引值 j 
    c.remove(i)     # 先將該小雞從串列中移出
    c.insert(j,e)   # 再插入老鷹到索引值j的位置
    e = i           # 老鷹換成被抓到的小雞
for i in c:         # 將c串列的每一隻小雞印出
    print('{} '.format(i),end='')  
