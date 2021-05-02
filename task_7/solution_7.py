s = input()
is_palindrom = True

for i in range(len(s) // 2):
    if s[i] != s[-i - 1]:
        is_palindrom = False
        break
print(is_palindrom)
