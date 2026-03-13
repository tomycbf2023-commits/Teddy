#k255. 鑿井取水 (Water)
n, w = map(int, input().split())
quota = 0

for day in range(1, n + 1):
    data = list(map(int, input().split()))
    usage = sum(data[1:])   

    quota = quota + w - usage

    if quota < 0:
        print(day)
        break
else:
    print(-1)
