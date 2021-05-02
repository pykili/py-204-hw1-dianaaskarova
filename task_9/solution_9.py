for n in range(1, 101):
    s = 0
    for i in range(1, n + 1):
        s += 2 * i - 1
    print(s == n * n)
