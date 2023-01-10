#!/usr/bin/python3

with open('input6', 'r') as f:
  summ = 0
  for l in f.readlines():
    i = 0
    three = []
    for lett in l:
      if len(three) == 4:
        print(three)
        summ += i
        break
      elif lett in three:
        print(three[three.index(lett)+1:])
        three = three[three.index(lett)+1:]
      three.append(lett)
      i += 1
  print(summ)
