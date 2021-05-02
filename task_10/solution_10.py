s = input()
new = list()
old = list()
for ch in s:
    new.insert(0, ch)
    old.append(ch)
print(new == old)
