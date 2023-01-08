#!/usr/bin/python3

summ = 0
summ_o = 0
with open('input4', 'r') as f:
  for line in f.readlines():
    a,b = line.split(',')
    (ax,ay) = (int(i) for i in a.split('-'))
    (bx,by) = (int(i) for i in b.split('-'))
    first_e = set([i for i in range(ax,ay+1)])
    second_e = set([i for i in range(bx,by+1)])
    if (len((first_e - second_e)) == 0 or len((second_e - first_e)) == 0):
      summ += 1
    if (len((first_e & second_e)) > 0 ):
      summ_o += 1

print(summ)
print(summ_o)

