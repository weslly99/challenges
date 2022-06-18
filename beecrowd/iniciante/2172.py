while True:
    a, b = [int(x) for x in input().strip().split()]
    xp = a * b
    if xp == 0:
        break
    print(xp)