n = int(input())
largest = 0
while 0 <= n and n <= 9:
    if n > largest:
        largest = n
    n = int(input())
print(largest)
