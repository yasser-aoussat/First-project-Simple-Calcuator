op = input("enter an operator '/ * - + ':")
n1 = float(input("enter the first number: "))
n2 = float(input("enter the second number: "))

if op == "+":
    result = n1 + n2
    print(result)
elif op == "-":
    result = n1 - n2
    print(result)
elif op == "*":
    result = n1 * n2
    print(result)
elif op == "/":
    result = n1 / n2
    print(result)
else :
    print("error")