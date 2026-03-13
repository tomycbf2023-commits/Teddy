#j179. 資料分類 (Classification)
def process_group(s):
    s = str(int(s))   # 去掉前導 0，"01" -> "1"
    if len(s) == 1:
        return int(s)
    return int(s[0]) * int(s[1])

a = input()

while True:
    a = str(int(a))   # 目前值正規化

    if len(a) == 1:
        print(a)
        break

    if len(a) == 4:
        left = process_group(a[:2])
        right = process_group(a[2:])
        a = str(int(str(left) + str(right)))

    elif len(a) == 3:
        x = int(a[0]) * int(a[1])
        y = int(a[1]) * int(a[2])
        a = str(int(str(x) + str(y)))

    else:  # len(a) == 2
        a = str(int(a[0]) * int(a[1]))
