#!/usr/bin/python3

elfs = []
with open('input1', 'r') as f:
  summ = 0
  for line in f.readlines():
    if line.strip():
      summ += int(line)
    else:
      elfs.append(summ)
      summ = 0

a = set(elfs)
print(max(a))

elfs.sort()
print(elfs[-1] + elfs[-2] + elfs[-3])
