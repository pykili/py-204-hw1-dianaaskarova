n = 10
l = []
for i in range(n):
    s = input()
    s_ = s.split()
    l.append(s_)
for inp in l:
    if inp[1] != inp[2]:
       print(inp[1], inp[2])
