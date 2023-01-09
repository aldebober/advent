#!/usr/bin/python3

stacks = {
  1: ['R', 'P', 'C', 'D', 'B', 'G'],
  2: ['H', 'V', 'G'],
  3: ['N', 'S', 'Q', 'D', 'J', 'P', 'M'],
  4: ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'],
  5: ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'],
  6: ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'],
  7: ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'],
  8: ['C', 'M', 'D', 'B', 'F'],
  9: ['F', 'C', 'Q', 'G']
}

stacks2 = stacks

with open('input5', 'r') as f:
  for instr in f.readlines():
    x = 0
    moves = []
    for i in instr.split():
      if x % 2 != 0:
        moves.append(int(i))
      x += 1
    a = moves[0]
    b = moves[1]
    c = moves[2]
    print(a,b,c)

    #for i in range(1,a+1):
    #  crate = stacks[b].pop()
    #  stacks[c].append(crate)

    for i in range(a, 0, -1):
      crate = stacks2[b].pop(-i)
      stacks2[c].append(crate)

top = []
top2 = []
#for i in range(1,10):
#  top.append(stacks[i][-1])
for i in range(1,10):
  top2.append(stacks2[i][-1])

print(''.join(top2))
