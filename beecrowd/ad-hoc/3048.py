n = int(input())
last = 0
count= 0
for i in range(n):
    num = int(input())
    if last != num:
        count += 1
        last = num
print(count)