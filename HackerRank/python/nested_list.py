from re import S


if __name__ == '__main__':
    students = []
    second_lower = None
    lower = None
    higther = None
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        if lower == None:
            lower = score
            second_lower = score
            higther = score
            continue
        if score <= lower:
            second_lower = lower
            lower = score
            print(f"1 - lower {lower} | second_lower{second_lower} | score {score}")
        elif score <= second_lower:
            second_lower = score
            print(f"2 - lower {lower} | second_lower{second_lower} | score {score}")

    names = list(filter(lambda x: x[1] == second_lower,students))
    names.sort(key=lambda x: x[0])

    print("______")
    print(second_lower)
    print(lower)
    for name,score in names:
        print(name)

"""    
harry
37.21
berry
37.21
tina
37.2
akriti
41
harsh
39

4
Sona
-25.001
Mona
-25.0001
Mini
-25.000
Rita
-25.0

4
Rachel
-50
Mawer
-50
Sheen
-50
Shaheen
51"""