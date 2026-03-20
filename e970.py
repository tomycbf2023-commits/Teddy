n = int(input())   # n 個數字
a = list(map(int, input().split()))   # 讀入 n 個數字放到串列a
b = a[n-1]         # 基數
sum = 0            # 找到的數字加總總和
for i in range(1,n+1): # 對應的索引值由 1 ~ n, 存在陣列的位置是 0 ~ n-1
    if i % b == 1:
        sum += a[i-1]  # 對應的索引值由 1 ~ n, 存在陣列的位置是 0 ~ n-1
m = sum % n
if m == 0:
    print(n,a[n-1])     
else:
    print(m,a[m-1])    
