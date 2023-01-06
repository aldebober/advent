#!/usr/bin/python3

# A for Rock
# B for Paper
# C for Scissors

# X for Rock
# Y for Paper
# Z for Scissors

# 1 for Rock
# 2 for Paper
# 3 for Scissors
# 0 if you lost
# 3 if the round was a draw
# 6 if you won

summ = 0
with open('input2', 'r') as f:
  for a in f.readlines():
    if ((a[0] == 'A' and a[2] == 'X') or (a[0] == 'B' and a[2] == 'Y') or (a[0] == 'C' and a[2] == 'Z')):
      summ += 3
      if a[2] == 'X':
        summ += 1
      elif a[2] == 'Y':
        summ += 2
      else:
        summ += 3
    elif ((a[0] == 'A' and a[2] == 'Z') or (a[0] == 'B' and a[2] == 'X') or (a[0] == 'C' and a[2] == 'Y')):
      summ += 0
      if a[2] == 'X':
        summ += 1
      elif a[2] == 'Y':
        summ += 2
      else:
        summ += 3
    else:
      summ += 6
      if a[2] == 'X':
        summ += 1
      elif a[2] == 'Y':
        summ += 2
      else:
        summ += 3

print(summ)

# A for Rock
# B for Paper
# C for Scissors
# 1 for Rock
# 2 for Paper
# 3 for Scissors
# X means you need to lose
# Y means you need to end the round in a draw
# Z means you need to win


summ = 0
with open('input2', 'r') as f:
  for a in f.readlines():
    if a[2] == 'X':
      summ += 0
      if a[0] == 'A':
        # you have Scissors
        summ += 3
      elif a[0] == 'B':
        # you have Rock
        summ += 1
      else:
        # you have Paper
        summ += 2
    elif a[2] == 'Y':
      summ += 3
      if a[0] == 'A':
        # you have Rock
        summ += 1
      elif a[0] == 'B':
        # you have Paper
        summ += 2
      else:
        # you have Scissors
        summ += 3
    else:
      summ += 6
      if a[0] == 'A':
        # you have Paper
        summ += 2
      elif a[0] == 'B':
        # you have Scissors
        summ += 3
      else:
        # you have Rock
        summ += 1

print(summ)
