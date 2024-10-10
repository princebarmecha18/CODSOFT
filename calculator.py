def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def multi(x,y):
    print(x*y)

def div(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("You cant divide by Zero")
    else:
        print(result)

def expo(x,y):
    print(x**y)

def fdiv(x,y):
    try:
        result=x//y
    except ZeroDivisionError:
        print("You cant divide by Zero")
    else:
        print(result) 

#MAIN
print("\nBasic Arithmetic Calculator\n")
print("This calculator performs\nAdditon(+)\nSubtraction(-)\nMultiplication(*)\nDivision(/)\nExponential(**)\nFloor Division(//)")

try:
    operand1=float(input("Enter First Number: "))
except ValueError:
    print("Enter an valid number!!")
    exit()

op=["+",'*','-','/','**','//']
operator=input("Enter the Operator: ")
if operator in op:
    pass
else:
    print("Enter a Valid Operator",op)
    exit()


try:
    operand2=float(input("Enter Second Number: "))
except ValueError:
    print("Enter an valid number!!")
    exit()

match operator:
    case "+":
        add(operand1,operand2)
    case "-":
        sub(operand1,operand2)
    case "*":
        multi(operand1,operand2)
    case "/":
        div(operand1,operand2)
    case "**":
        expo(operand1,operand2)
    case "//":
        fdiv(operand1,operand2)