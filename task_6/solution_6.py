n = int(input())
if n != 0:
    print('_')
for i in range(n):
    if i == n-1:
        print((2*i + 1)*' '+'|')
    else:
        print((2*i + 1)*' '+'|_')
