#!/usr/bin/python3

small_letters = map(chr, range(ord('a'), ord('z')+1))
big_letters = map(chr, range(ord('A'), ord('Z')+1))
letters = list(small_letters) + list(big_letters)

summ = 0
with open('input3', 'r') as f:
  for line in f.readlines():
    a = line[:int(len(line)/2)]
    b = line[int(len(line)/2):]
    lit = ''.join(set(a) & set(b))
    summ += letters.index(lit) + 1

print(summ)

summ = 0
y = 0
three = {}
three[y] = []
with open('input3', 'r') as f:
  i = 0
  for line in f.readlines():
    if i % 3 == 0 and i != 0:
      y += 1
      three[y] = []
    three[y].append(line.strip())
    i += 1
print(three)

for l in three.values():
  for letter in (set(l[2]) & set(l[1]) & set(l[0])):
    print(letters.index(letter), letter)
    summ += letters.index(letter) + 1

print(summ)
