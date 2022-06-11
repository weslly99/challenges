t = int(input())
resp = [ int(x) for x in input().split()]
corrects = 0
for i in resp:
    if i == t:
        corrects += 1
print(corrects)