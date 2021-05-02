left = input()
right = input()
ln = len(left)
rn = len(right)
i = 0
is_there = False
while i <= rn - ln:
    if right[i:i+ln] == left:
        is_there = True
        break
    i += 1
print(is_there)
