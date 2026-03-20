while 1:
  a = list(map(int, input().split()))
  if a[0]==-1:
    break
  n = a[0]
  e = a[1]
  days = 0
  foods = n*e
  eats = 0
  while foods > 0:
    days += 1
    foods -= n
    eats += n
    while eats >= e:
      n -= 1
      eats -= e
  print(days)    
