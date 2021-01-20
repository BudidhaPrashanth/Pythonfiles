def calculator():
    n1 = int(input("enter first num : "))
    symbol = input("enter symbol : ")
    n2 = int(input("enter second num : "))

    if symbol == "+":
        print(n1+n2)
    elif symbol == "-":
        print(n1-n2)
    elif symbol == "*":
        print(n1*n2)
    elif symbol == "/":
        print(n1/n2)
    elif symbol == "%":
        print(n1%n2)
calculator()