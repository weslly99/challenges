n = int(input())
total = 0
for i in range(n):
    t, c = [int(i) for i in input().split()]
    total += (t * c)
print(total)