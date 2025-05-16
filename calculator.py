# Simple Calculator

def calculator():
    print("Select Operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponent")
    print("7. Floor Division")
    print("8. Square Root")
    print("9. Cube Root")
    print("10. Logarithm")
    print("11. Factorial")
    print("12. Exit")
    
    choice = input("Enter choice (1 - 12): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if(choice == "1"):
        print(f"{num1} + {num2} = {num1 + num2}")
    
    elif(choice == "2"):
        print(f"{num1} - {num2} = {num1 - num2}")
        
    elif(choice == "3"):
        print(f"{num1} * {num2} = {num1 * num2}")
        
    elif(choice == "4"):
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
            
    elif(choice == "5"):
        print(f"{num1} % {num2} = {num1 % num2}")
        
    elif(choice == "6"):
        print(f"{num1} ** {num2} = {num1 ** num2}")
        
    elif(choice == "7"):
        print(f"{num1} // {num2} = {num1 // num2}")
        
    elif(choice == "8"):
        if num1 < 0:
            print("Error! Square root of negative number.")
        else:
            print(f"Square root of {num1} = {num1 ** 0.5}")
            
    elif(choice == "9"):
        if num1 < 0:
            print("Error! Cube root of negative number.")
        else:
            print(f"Cube root of {num1} = {num1 ** (1/3)}")
            
    elif(choice == "10"):
        import math
        if num1 <= 0:
            print("Error! Logarithm of non-positive number.")
        else:
            print(f"Logarithm of {num1} = {math.log(num1, num2)}")
            
    elif(choice == "11"):
        import math
        if num1 < 0:
            print("Error! Factorial of negative number.")
        else:
            print(f"Factorial of {int(num1)} = {math.factorial(int(num1))}")
            
    elif(choice == "12"):
        print("Exiting the calculator.")
        return
    
    else:
        print("Invalid input! Please try again.")
        
if __name__ == "__main__":
    calculator()
    
    
    