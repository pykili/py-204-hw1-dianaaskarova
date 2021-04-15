n = 10
l = []
front_vow = 'eiöü'
back_vow = 'aıou'
for i in range(n):
    s = input()
    s_ = s.split()
    l.append(s_)
for inp in l:
    if inp[1] != inp[2] and inp[1].startswith(inp[2]):
        want = ''
        yes = 0
        no = 0
        for ch in reversed(inp[2]):
            if ch in front_vow + back_vow:
                if ch in front_vow:
                    want = front_vow
                    break
                else:
                    want = back_vow
                    break
        for ch in inp[1]:
            if ch in front_vow + back_vow:
                if ch not in want:
                    no += 1
                else:
                    yes += 1
        print(no==0, yes, no)
