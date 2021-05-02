s = input()
occured_twice = False
for i in range(len(s) - 1):
    if s.count(s[i:i+2]) > 1:
        occured_twice = True
print(occured_twice)
