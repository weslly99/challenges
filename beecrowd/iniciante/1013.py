a, b, c = [int(v) for v in input().strip().split()]
maior = (a + b + abs(a-b)) // 2
maior = (maior + c + abs(maior - c)) // 2
print(f"{maior} eh o maior")