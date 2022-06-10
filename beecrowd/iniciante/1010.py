cod1, value1, num1 = input().strip().split()
cod2, value2, num2 = input().strip().split()
total = (float(value1) * float(num1)) + (float(value2) * float(num2))
print("VALOR A PAGAR: R$ {:.2f}".format(total))