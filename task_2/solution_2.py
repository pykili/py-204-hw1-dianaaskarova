user_input = input()
ma = -1
for ch in user_input:
    if(user_input.count(ch) > ma):
        ma = user_input.count(ch)
        char = ch
print(char)
