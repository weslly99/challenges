if __name__ == "__main__":
    name = input()
    salary = float(input())
    bonus = float(input())
    print("TOTAL = R$ {:.2f}".format(salary + (bonus * 0.15)))