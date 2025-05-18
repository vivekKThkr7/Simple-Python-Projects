# number  = int(input("Enter any whole number: "))
# sum = 0

# while number > 0:
#     digit = number % 10
#     sum += digit
#     number = number // 10
    
# print(f"Sum of digits is {sum}")


# Sum of digits
number = int(input("Enter any number: "))
sum = 0

while number > 0:
    digit = number % 10
    sum += digit
    number = number // 10
    
    
print(f"Sum of digits is {sum}")