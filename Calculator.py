print("Number -> Operation -> Number = Output")
def CalculatorFunct(num1, operation, num2):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2
        case "**":
            return num1 ** num2
        case "//":
            return num1 // num2

while True:
    print("The answer is: ", CalculatorFunct(int(input("")), input(""), int(input(""))))
    print("Number -> Operation -> Number = Output")